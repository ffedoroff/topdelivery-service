from service import service


@service.route('/')
@service.route('/index')
def index():
    return "Homepage"
