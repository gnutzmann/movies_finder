from .dbconnection import get_database
from movies_finder import app
from bson.json_util import dumps


@app.route('/')
@app.route('/index')
def index():
    return '''<html> <head> <title>Movies finder</title> </head> <body>
    <h1>Movies Finder</h1> </body> </html>'''


@app.route('/movies')
def movies():
    collection = get_database()['movies_collection']
    cursor = collection.find()
    list_cur = list(cursor)

    json_data = dumps(list_cur)

    return json_data


@app.route('/movie/<id>')
def movie(id):
    collection = get_database()['movies_collection']
    cursor = collection.find({'ID': int(id)})
    list_cur = list(cursor)

    json_data = dumps(list_cur)

    return json_data


@app.route('/movie_name/<movie_name>')
def movie_name(movie_name):
    collection = get_database()['movies_collection']
    cursor = collection.find({'Title': str(movie_name)})
    list_cur = list(cursor)

    json_data = dumps(list_cur)

    return json_data
