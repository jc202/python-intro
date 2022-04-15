def get_movies():
    movies = []
    
    try:
        with open ("examples/mar24/movies.txt") as file:
            for line in file:
                movies.append(line.strip())
    except FileNotFoundError:
        print("Sorry, your movies could not be loaded.") 
           
    return movies

my_movies = get_movies()

for movie in my_movies:
    print(movie)