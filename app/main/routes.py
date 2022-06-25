from app.main import main


@main.route('/')
@main.route('/index')
def index():
    return 'Hello world!'
