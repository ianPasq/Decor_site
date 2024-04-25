from flask import Flask, jsonify, request
from flask_cors import CORS
from __init__ import create_app, db

app = create_app('development')
CORS(app)

cart_items = {
    'chair': 10,
    'table': 7,
    'carpet': 9,
    'decoration': 12,
}

def get_total_price():
    price = {
        'chair': 20,
        'table': 110,
        'carpet': 45,
        'decoration': 30,
    }
    total_price = sum(price[item] * quantity for item, quantity in cart_items.items())
    return round(total_price, 2)

@app.route('/cart', methods=['GET'])
def cart():
    total_price = get_total_price()
    return jsonify({
        'cart_contents': cart_items,
        'total_price': total_price,
    })
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    item = data['item']
    quantity = data['quantity']
    cart_items[item] = cart_items.get(item, 0) + quantity
    total_price = get_total_price()
    return jsonify({
        'cart_contents': cart_items,
        'total_price': total_price,
    })
if __name__ == '__main__':
    app.run(debug=True)