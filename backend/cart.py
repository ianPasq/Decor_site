from flask import Blueprint, jsonify, request, current_app
from datetime import datetime
from app import db
from models import Product, Order, OrderItem


cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/add_cart', methods=['PUT'])
def add_cart():
    try:
        current_app.logger.info("Received add_cart request: %s", request.json)
        data = request.json
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        product = Product.query.get(product_id)
        if not product:
            return jsonify({'message': 'Product not found'}), 404

        cart = Order.query.filter_by(user_id=user_id, status='active').first()
        if not cart:
            cart = Order(user_id=user_id, date_ordered=datetime.utcnow())
            db.session.add(cart)
            db.session.commit()

        order_item = OrderItem.query.filter_by(
            order_id=cart.id,
            product_id=product_id
        ).first()

        if order_item:
            order_item.quantity += quantity
        else:
            order_item = OrderItem(
                order_id=cart.id,
                product_id=product.id,
                quantity=quantity,
                price=product.price
            )
            db.session.add(order_item)

        db.session.commit()
        return jsonify({'message': 'Product added to cart successfully'}), 200

    except Exception as e:
        current_app.logger.error(f"Error in add_cart: {e}")
        db.session.rollback()
        return jsonify({'message': 'Server error'}), 500
    
def update_cart(cart, product_id, quantity):
    order_item = OrderItem.query.filter_by(order_id=cart.id, product_id=product_id).first()
    if quantity <= 0:
        db.session.delete(order_item)
    else:
        order_item.quantity += quantity
    db.session.commit()

def add_to_cart(cart, product, quantity):
    try:
        price = product.price
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

    cart = Order.query.filter_by(user_id=user_id, status='active').first()
    if not cart:
        return jsonify({'message': 'Cart not found'}), 404

    item = OrderItem.query.filter_by(
        order_id=cart.id,
        product_id=product_id
    ).first()
    if not item:
        return jsonify({'message': 'Product not in cart'}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Product removed from cart'}), 200

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
    products = []
    for prod in products:
        p = Product(
            name=prod['name'],
            price=prod['price'],
            category=prod['category'],
            img=prod['img']
        )
        db.session.add(p)
    db.session.commit()
    return jsonify({'message': 'Products seeded successfully'}), 200

@cart_bp.route('/view_cart', methods=['GET'])
def view_cart():
    user_id = request.args.get('user_id')
    cart = Order.query.filter_by(user_id=user_id, status='active').first()
    if not cart:
        return jsonify({'cart_contents': []}), 200

    items = OrderItem.query.filter_by(order_id=cart.id).all()
    payload = []
    for itm in items:
        prod = Product.query.get(itm.product_id)
        payload.append({
            'product_id': itm.product_id,
            'name': prod.name,
            'quantity': itm.quantity,
            'price': itm.price,
            'img': prod.img
        })
    return jsonify({'cart_contents': payload}), 200
    

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


