import requests
import random

API_KEY = "a3c75ab7d70b7bca4699dab522e17a9b"
BASE_URL = "https://api.themoviedb.org/3"


def get_genre_id(genre_name):
    """Get the genre ID from the genre name."""
    url = f"{BASE_URL}/genre/movie/list"
    params = {"api_key": API_KEY, "language": "en-US"}
    response = requests.get(url, params=params)
    data = response.json()

    for genre in data['genres']:
        if genre['name'].lower() == genre_name.lower():
            return genre['id']
    return None


def get_movies_by_genre(genre_id):
    """Get a list of movies based on genre ID."""
    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY,
        "with_genres": genre_id,
        "sort_by": "popularity.desc",
        "language": "en-US",
        "page": random.randint(1, 5)  
    }
    response = requests.get(url, params=params)
    return response.json().get("results", [])


def recommend_movie():
    """Ask the user for a genre and recommend a random movie."""
    genre_name = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")
    genre_id = get_genre_id(genre_name)

    if not genre_id:
        print("Sorry, that genre was not found.")
        return

    movies = get_movies_by_genre(genre_id)

    if not movies:
        print("No movies found for that genre.")
        return

    movie = random.choice(movies)
    print(f"\n🎬 Recommended Movie: {movie['title']}")
    print(f"📝 Overview: {movie.get('overview', 'No description available')}")
    print(f"⭐ Rating: {movie.get('vote_average', 'N/A')}")
    print(f"📅 Release Date: {movie.get('release_date', 'N/A')}")

if __name__ == "__main__":
    recommend_movie()
