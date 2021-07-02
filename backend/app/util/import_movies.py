import pandas as pd

cols = ['ID', 'Title', 'Year', 'Age', 'IMDb', 'Rotten Tomatoes', 'Netflix', 'Hulu',
        'Prime Video', 'Disney+', 'Type', 'Directors', 'Genres', 'Country', 'Language', 'Runtime']

movies = pd.read_csv('../../data/movies.csv', header=0, sep=',', usecols=cols)

print(movies.head(20))

moviesList = movies.to_dict('records')

print(moviesList)
