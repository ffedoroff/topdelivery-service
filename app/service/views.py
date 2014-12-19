from service import service
from flask import render_template


@service.route('/')
@service.route('/index')
def index():
    return render_template("index.html")
