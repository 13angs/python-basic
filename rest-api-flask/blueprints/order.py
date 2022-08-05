from flask import Blueprint, jsonify

order_bp = Blueprint('order', __name__)


all_orders = [
    {'id': 1, 'uid': 'uid1', 'name': 'order 1'},
    {'id': 2, 'uid': 'uid2', 'name': 'order 2'},
]

@order_bp.before_request
def before_req():
    print("This will execute before the request")

    # fetch the data sent with the request
    # print(request.data)
    # print(request.args)

@order_bp.route('/', methods=['GET'])
def order_list():
    return jsonify(all_orders), 200

@order_bp.route('/<int:order_id>/')
def order_detail_id(order_id):
    # find the object in list by id
    result = next((item for item in all_orders if item['id'] == order_id), {'status': 404, 'message': 'not found'})
    return jsonify(result), 200

@order_bp.route('/<string:order_uid>/')
def order_detail_uid(order_uid):
    # find the object in list by id
    result = next((item for item in all_orders if item['uid'] == order_uid), {'status': 404, 'message': 'not found'})
    return jsonify(result), 200