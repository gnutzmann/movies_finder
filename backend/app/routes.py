from .dbconnection import db
from movies_finder import app
from bson.json_util import dumps
from flask import Response


@app.route('/')
@app.route('/index')
def index():
    return '''<html> <head> <title>Movies finder</title> </head> <body>
    <h1>Movies Finder</h1> </body> </html>'''


@app.route('/movies', methods=['GET'])
def movies():
    collection = db['movies_collection']
    cursor = collection.find()
    list_cur = list(cursor)

    json_data = Response(dumps((list_cur), default=str),
                         mimetype="application/json")

    return json_data


@app.route('/movie/id/<id>', methods=['GET'])
def movie_id(id):
    collection = db['movies_collection']
    cursor = collection.find({'ID': int(id)})
    list_cur = list(cursor)

    json_data = Response(dumps((list_cur), default=str),
                         mimetype="application/json")

    return json_data


@app.route('/movie/title/<title>', methods=['GET'])
def movie_title(title):
    collection = db['movies_collection']
    cursor = collection.find({'Title': {"$regex": str(title)}})
    list_cur = list(cursor)

    json_data = Response(dumps((list_cur), default=str),
                         mimetype="application/json")

    return json_data


@app.route('/movie/director/<director>', methods=['GET'])
def movie_director(director):
    collection = db['movies_collection']
    cursor = collection.find({'Directors': {"$regex": str(director)}})
    list_cur = list(cursor)

    json_data = Response(dumps((list_cur), default=str),
                         mimetype="application/json")

    return json_data
