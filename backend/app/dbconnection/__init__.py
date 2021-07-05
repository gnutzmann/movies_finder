def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb://localhost"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['movies']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    dbname = get_database()
