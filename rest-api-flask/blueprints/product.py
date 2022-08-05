from flask import Blueprint, jsonify

product_bp = Blueprint('product', __name__)


all_products = [
    {'id': 1, 'uid': 'uid1', 'name': 'product 1'},
    {'id': 2, 'uid': 'uid2', 'name': 'product 2'},
]

@product_bp.before_request
def before_req():
    print("This will execute before the request")

    # fetch the data sent with the request
    # print(request.data)
    # print(request.args)

@product_bp.route('/', methods=['GET'])
def product_list():
    return jsonify(all_products), 200

@product_bp.route('/<int:product_id>/')
def product_detail_id(product_id):
    # find the object in list by id
    result = next((item for item in all_products if item['id'] == product_id), {'status': 404, 'message': 'not found'})
    return jsonify(result), 200

@product_bp.route('/<string:product_uid>/')
def product_detail_uid(product_uid):
    # find the object in list by id
    result = next((item for item in all_products if item['uid'] == product_uid), {'status': 404, 'message': 'not found'})
    return jsonify(result), 200