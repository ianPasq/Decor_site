from flask import Flask, jsonify, request
from flask_cors import CORS
from __init__ import create_app, db
from models import Order, OrderItem, Product
from datetime import datetime

app = create_app('development')
CORS(app)

@app.route('/add_cart', methods=['PUT'])
def add_cart():
    data = request.json
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    cart = Order.query.filter_by(user_id=user_id).first()
    if not cart:
        cart = Order(user_id=user_id, date_ordered=datetime.now())
        db.session.add(cart)
        db.session.commit()
        
    order_item = OrderItem.query.filter_by(order_id=cart.id, product_id=product_id).first()
    if order_item:
        update_cart(cart, product_id, quantity)
    else:
        add_to_cart(cart, product, quantity)
    
    return jsonify({'message': 'Product added to cart successfully'}), 200
    
def update_cart(cart, product_id, quantity):
    order_item = OrderItem.query.filter_by(order_id=cart.id, product_id=product_id).first()
    if quantity <= 0:
        db.session.delete(order_item)
    else:
        order_item.quantity += quantity
    db.session.commit()

def add_to_cart(cart, product, quantity):
    order_item = OrderItem(order_id=cart.id, product_id=product.id, quantity=quantity, price=product.price)
    db.session.add(order_item)
    db.session.commit()
    
    

@app.route('/delete_cart', methods=['DELETE'])
def delete_cart():
    data = request.json
    user_id = data.get(user_id)
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
    

@app.route('/view_cart', methods=['GET'])
def view_cart():
    user_id = request.args.get('user_id')
    
    cart = Order.query.filter_by(user_id=user_id).first()
    if not cart:
        return jsonify({'message': 'Cart not found for the user'}), 404
    
    items = OrderItem.query.filter_by(order_id=cart.id).all()
    
    cart_contents = []
    for item in items:
        product = Product.query.get(item.product_id)
        cart_contents.append({
            'product_id': item.product_id,
            'name': product.name,
            'quantity': item.quantity,
            'price': item.price
        })
    
    return jsonify({'cart_contents': cart_contents}), 200
    

@app.route('/edit_cart', methods=["PUT"])
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
