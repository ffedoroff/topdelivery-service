from service import service
from flask import render_template


@service.route('/')
@service.route('/index')
def index():
    return render_template("index.html")

@service.route('/order/', methods=['GET'])
def order_list():
    return "orders list response"


@service.route('/order/<order_id>', methods=['GET'])
def order(order_id):
    return "order {0} details".format(order_id)
