from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Days'}
    return '''<html> <head> <title>Movies finder</title> </head> <body>
    <h1>Viu, tá funcionando ''' + user['username']
    + '''!</h1> </body> </html>'''
