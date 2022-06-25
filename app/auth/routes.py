from app.auth import auth


@auth.route('/login')
def index():
    return 'Login!'
