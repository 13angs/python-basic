from flask import Flask

from blueprints.product import product_bp
from blueprints.order import order_bp

app = Flask(__name__)

app.register_blueprint(product_bp, url_prefix='/api/v1/products')
app.register_blueprint(order_bp, url_prefix='/api/v1/orders')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)