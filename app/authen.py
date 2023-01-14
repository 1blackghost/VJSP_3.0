#This is used for signup,signin,and logout routes of user
#It will include verfication email verfication process,forgot password and many more.

from main import app

@app.route('/login')
def login():
    return 'login page'

@app.route('/signup')
def signup():
    return 'signup'
@app.route('/logout')
def logout():
    return 'logout'