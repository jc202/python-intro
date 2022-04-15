#Author: Justin C
from movie import Movie

def get_movies():
    movies = []
    
    with open("assignments/ass24/movies.txt") as file:
       for line in file:
        data = line.split(',')
        title = data[0].strip()
        description = data[1].strip()
        actors = data[2].strip().split('*')
        genre = data[3].strip().lower()
        rating = data[4].strip()
        movies.append(Movie(title, description, actors, genre, rating))
    return movies

movie_list = get_movies()
print("***** Movie Listings *****")

while True:
    command = input("(L)ist all movies, get movie (D)etails, or (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command == "l":
        for movie in movie_list:
            movie.display_movie()
    elif command == "d":
        user_search = input("Enter movie name: ")
        for movie in movie_list:
            if movie.is_match(user_search):
                movie.display_movie()
                break
        else:
            print("Sorry, we don't seem to have that movie in our listing.")
    else:
        print("Invalid Command.")
            
print("Goodbye.")