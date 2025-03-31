from flask import Blueprint, jsonify, request
from datetime import datetime
from app import db
from models import Product, Order, OrderItem


cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/add_cart', methods=['PUT'])
def add_cart():
    try:
        app.logger.info("Received add_cart request: %s", request.json)
        data = request.json
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        app.logger.info(f"Looking for product {product_id}")
        product = Product.query.get(product_id)
        if not product:
            app.logger.error("Product not found")
            return jsonify({'message': 'Product not found'}), 404

        app.logger.info(f"Product found: {product.name}")
        app.logger.info(f"Checking cart for user {user_id}")
        cart = Order.query.filter_by(user_id=user_id).first()
        
        if not cart:
            app.logger.info("Creating new cart")
            cart = Order(user_id=user_id, date_ordered=datetime.now())
            db.session.add(cart)
            db.session.flush()
            db.session.refresh(cart)
            
        order_item = OrderItem.query.filter_by(order_id=cart.id, product_id=product_id).first()
        if order_item:
            update_cart(cart, product_id, quantity)
        else:
            add_to_cart(cart, product, quantity)
    
        return jsonify({'message': 'Product added to cart successfully'}), 200

    except Exception as e:
        app.logger.error(f"Error in add_cart: {str(e)}")
        return jsonify({'message': f'Server error: {str(e)}'}), 500
    
def update_cart(cart, product_id, quantity):
    order_item = OrderItem.query.filter_by(order_id=cart.id, product_id=product_id).first()
    if quantity <= 0:
        db.session.delete(order_item)
    else:
        order_item.quantity += quantity
    db.session.commit()

def add_to_cart(cart, product, quantity):
    try:
        price = float(str(product.price).replace('$', '').strip())
        order_item = OrderItem(
            order_id=cart.id,
            product_id=product.id,
            quantity=quantity,
            price=price
        )

        db.session.add(order_item)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Invalid price format: {product.price}") from e
    
    

@cart_bp.route('/delete_cart', methods=['DELETE'])
def delete_cart():
    data = request.json
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    
    cart = Order.query.filter_by(user_id=user_id).first()
    if not cart:
        return jsonify({'message': 'Cart not found for the user'}), 404
    
    order_item = OrderItem.query.filter_by(order_id=cart.id, product_id=product_id).first()
    if not order_item:
        return jsonify({'message': 'Product not found in the cart'}), 404
    
    db.session.delete(order_item)
    db.session.commit()
    
    return jsonify({'message': 'Product deleted from cart successfully'}), 200

@cart_bp.route('/debug_products')
def debug_products():
    products = Product.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'category': p.category
    } for p in products])

@cart_bp.route('/seed_products', methods=['POST'])
def seed_products():
    products = [
        {
            "id": 1,
            "category": "Furniture",
            "name": "Comfortable Dark Gray Chair and Table",
            "price": 1000.00,
            "img": "./assets/comfort-chair-and-table.avif"
        },
        {
            "id": 2,
            "category": "Furniture",
            "name": "Fancy Black and Gold Metal Chair and Glass Table",
            "price": 1500.00,
            "img": "./assets/fancy-chair-and-table.avif"
        },
        {
            "id": 3,
            "category": "Furniture",
            "name": "Wide Comfortable Gray Living Room Chair",
            "price": 300.00,
            "img": "./assets/living-room-chair.avif"
        },
        {
            "id": 4,
            "category": "Furniture",
            "name": "Minimalistic Wooden Chair and Table",
            "price": 1200.00,
            "img": "assets/minimalistic-chair-and-table-wood.avif"
        },
        {
            "id": 5,
            "category": "Furniture",
            "name": "Lether Office Chair",
            "price": 1200.00,
            "img": "assets/lether-office-chair.avif"
        },
        {
            "id": 6,
            "category": "Furniture",
            "name": "Minimal Black Metal and Wood Chair",
            "price": 1200.00,
            "img": "assets/minimalistic-metal-and-wood-chair.avif"
        },
        {
            "id": 7,
            "category": "Furniture",
            "name": "Simple White Chair",
            "price": 1200.00,
            "img": "assets/white-simple-chair.avif"
        },
        {
            "id": 8,
            "category": "Furniture",
            "name": "Simple Small White Wooden bedside Table",
            "price": 1200.00,
            "img": "assets/white-wooden-bed-table.avif"
        },
        {
            "id": 9,
            "category": "Furniture",
            "name": "Alternative Minimal and Comfortable Yellow Chair",
            "price": 1500.00,
            "img": "assets/yellow-chair.avif"
        }
    ]
    
    for prod in products:
        product = Product(
            id=prod['id'],
            name=prod['name'],
            price=prod['price'],
            category=prod['category'],
            img=prod['img']
        )
        db.session.add(product)
    
    db.session.commit()
    return jsonify({'message': 'Products seeded successfully'}), 200

@cart_bp.route('/view_cart', methods=['GET'])
def view_cart():
    user_id = request.args.get('user_id')
    
    cart = Order.query.filter_by(user_id=user_id).first()
    if not cart:
        return jsonify({'cart_contents': []}), 200
    
    items = OrderItem.query.filter_by(order_id=cart.id).all()
    
    cart_contents = []
    for item in items:
        product = Product.query.get(item.product_id)
        cart_contents.append({
            'product_id': item.product_id,
            'name': product.name,
            'quantity': item.quantity,
            'price': item.price,
            'img': product.img
        })
    
    return jsonify({'cart_contents': cart_contents}), 200
    

@cart_bp.route('/edit_cart', methods=["PUT"])
def edit_cart():
    data = request.json
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    new_quantity = data.get('quantity')
    
    if not user_id or not product_id or new_quantity is None:
        return jsonify({'message': 'User ID, Product ID, and New Quantity are required'}), 400
    
    cart = Order.query.filter_by(user_id=user_id).first()
    if not cart:
        return jsonify({'message': 'Cart not found for the user'}), 404
    
    order_item = OrderItem.query.filter_by(order_id=cart.id, product_id=product_id).first()
    if not order_item:
        return jsonify({'message': 'Product not found in the cart'}), 404
    
    order_item.quantity = new_quantity
    db.session.commit()
    
    return jsonify({'message': 'Cart updated successfully'}), 200



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
