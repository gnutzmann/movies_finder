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


@app.route('/movie/id/<id>')
def movie_id(id):
    collection = get_database()['movies_collection']
    cursor = collection.find({'ID': int(id)})
    list_cur = list(cursor)

    json_data = dumps(list_cur)

    return json_data


@app.route('/movie/title/<title>')
def movie_title(title):
    collection = get_database()['movies_collection']
    cursor = collection.find({'Title': {"$regex": str(title)}})
    list_cur = list(cursor)

    json_data = dumps(list_cur)

    return json_data


@app.route('/movie/director/<director>')
def movie_director(director):
    collection = get_database()['movies_collection']
    cursor = collection.find({'Directors': {"$regex": str(director)}})
    list_cur = list(cursor)

    json_data = dumps(list_cur)

    return json_data
