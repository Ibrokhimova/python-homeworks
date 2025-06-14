import pandas as pd
iris = pd.read_json('iris.json')
iris.columns = iris.columns.str.lower()
iris_selected = iris[['sepal_length', 'sepal_width']]
print("Selected columns from iris.json:")
print(iris_selected.head())
titanic = pd.read_excel('titanic.xlsx')
titanic_over_30 = titanic[titanic['Age'] > 30]
print("\nTitanic passengers with age > 30:")
print(titanic_over_30.head())
gender_counts = titanic['Sex'].value_counts()
print("\nGender counts in Titanic dataset:")
print(gender_counts)

flights = pd.read_parquet('flights.parquet')

flights_subset = flights[['origin', 'dest', 'carrier']]
print("\nSelected columns from flights.parquet:")
print(flights_subset.head())
unique_dest_count = flights['dest'].nunique()
print("\nNumber of unique destinations:", unique_dest_count)
movies = pd.read_csv('movie.csv')
long_movies = movies[movies['duration'] > 120]
sorted_long_movies = long_movies.sort_values(by='director_facebook_likes', ascending=False)
print("\nMovies with duration > 120 mins, sorted by director_facebook_likes:")
print(sorted_long_movies[['title', 'duration', 'director_facebook_likes']].head())
