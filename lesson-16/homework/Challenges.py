import pandas as pd
iris = pd.read_json('iris.json')
print("Iris Dataset - Mean:")
print(iris.mean(numeric_only=True))

print("\nIris Dataset - Median:")
print(iris.median(numeric_only=True))

print("\nIris Dataset - Standard Deviation:")
print(iris.std(numeric_only=True))
titanic = pd.read_excel('titanic.xlsx')
print("\nTitanic Dataset – Age Statistics:")
print("Min Age:", titanic['Age'].min())
print("Max Age:", titanic['Age'].max())
print("Sum of Ages:", titanic['Age'].sum())
movies = pd.read_csv('movie.csv')
likes_by_director = movies.groupby('director_name')['director_facebook_likes'].sum()
top_director = likes_by_director.idxmax()
top_likes = likes_by_director.max()

print("\nDirector with highest total Facebook likes:")
print(f"{top_director} – {top_likes} likes")

longest_movies = movies[['title', 'director_name', 'duration']].sort_values(by='duration', ascending=False).head(5)
print("\nTop 5 Longest Movies and Their Directors:")
print(longest_movies)
flights = pd.read_parquet('flights.parquet')
print("\nFlights Dataset – Missing Values:")
print(flights.isnull().sum())

if 'dep_delay' in flights.columns:
    mean_dep_delay = flights['dep_delay'].mean(skipna=True)
    flights['dep_delay'].fillna(mean_dep_delay, inplace=True)
    print("\nMissing 'dep_delay' values filled with mean.")
else:
    print("\nColumn 'dep_delay' not found in dataset.")
