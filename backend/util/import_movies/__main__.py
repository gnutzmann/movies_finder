import datetime
import pandas as pd



def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb://localhost"

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)
    return client['movies']


def import_csv(filename, cols):
    try:
        return pd.read_csv(filename, header=0, sep=',', usecols=cols)
    except (FileNotFoundError):
        return []


if __name__ == '__main__':
    movies = import_csv('../data/movies.csv', ['ID', 'Title', 'Year', 'Age',
                                               'IMDb', 'Rotten Tomatoes',
                                               'Netflix', 'Hulu',
                                               'Prime Video', 'Disney+',
                                               'Type', 'Directors',
                                               'Genres', 'Country', 'Language',
                                               'Runtime'])
    #datetime.timedelta(hours=-3))
    movies['created_at'] = datetime.datetime.utcnow()
    movies['updated_at'] = datetime.datetime.utcnow()
    
    if len(movies) > 0:
        moviesList = movies.to_dict('records')

        dbname = get_database()
        collection_name = dbname["movies_collection"]
        collection_name.insert_many(moviesList)
        print('Dados importados!')
    else:
        print('Arquivo CSV não encontrado!')
