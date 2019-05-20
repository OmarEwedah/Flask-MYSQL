from flask import  Flask, abort, jsonify
from flask import request
from model import db
from model import engine
from model import app as application
import simplejson as json
from sqlalchemy.exc import IntegrityError
import os
import request_helpers
import model

# initate flask app
app = Flask(__name__)


@app.route('/shoppingBasket/addItemToBasket', methods=['POST'])
def shopping_basket():

        if not request.json or ('item_id' or 'basket_id' or 'item_quantity') not in request.json:
            abort(400, {'message': 'required parameters are missing'})

        if not request_helpers.check_item_exist(engine, request.get_json()['item_id']):
            abort(404, {'message': 'item not exist'})

        if not request_helpers.change_item_quantity(engine, request.get_json()['item_id'], request.get_json()['item_quantity']):
            abort(400, {'message': 'item quantity not available'})

        else:
            data = request.get_json()
            request_helpers.add_shopping_basket(data['basket_id'], engine)
            request_helpers.update_cart_price_quantity(engine, data['item_id'], data['basket_id'], data['item_quantity'])
            request_helpers.add_item_to_basket(engine, data['item_id'], data['basket_id'])
            return jsonify(
                status=202,
                content_type='application/json',
                message='item added to cart successfully')



@app.route('/shoppingBasket/<shopping_cart_id>', methods=['GET'])
def shopping_basket_total(shopping_cart_id):
    cart = request_helpers.retrieve_total_price_from_basket(engine, shopping_cart_id)
    items_in_cart = request_helpers.retrieve_all_items_from_basket(engine, shopping_cart_id)
    return jsonify({
        "status": 200,
        "Total_price": cart[1],
        "Total_quantity": cart[2],
        "items": items_in_cart
    })



@app.route('/shoppingBasket/AddItem', methods=['POST'])
def addItem():
    data = request.get_json()
    engine.execute("INSERT INTO shoppingBasket.Items (item_name, item_price, item_quantity) VALUES (%s, %s, %s)", data['item_name'], data['item_price'],data['item_quantity'])
    return jsonify(
        status=202,
        message='item added to successfully')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
