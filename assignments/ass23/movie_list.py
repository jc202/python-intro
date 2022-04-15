#Author: Justin C
from movie import Movie

movie_list = (
    Movie("Parent Trap", "Identical twins Annie and Hallie, separated at birth and each raised by one of their biological parents, discover each other for the first time at summer camp and make a plan to bring their wayward parents back together.", "Lindsay Lohan, Dennis Quad, Natasha Richardson", "Comedy", "6.6"),
    Movie("Divergent", "In a future society, people are divided into factions based on their personalities. After a young woman learns she is a Divergent and will never fit into any one group, she uncovers a conspiracy to destroy all those like her.", "Shailene Woodley, Theo James, Ashley Judd, Jai Courtney, Ray Stevenson, Zoe Kravitz, Miles Teller, Tony Goldwyn, Ansel Elgort, Maggie Q", "Action", "6.7"),
    Movie("The Polar Express", "A boy takes a magical train ride to the North Pole on Christmas Eve and discovers the enchanting wonders of friendship and the holiday spirit.", "Tom Hanks, Nona Gaye, Peter Scolari, Eddie Deezen, Michael Jeter", "Children & Family", "6.6"),
    Movie("The Clark Sisters", "With guidance from their mother, five siblings overcome humble beginnings to form the renowned gospel group the Clark Sisters.", "Aunjanue Ellis, Kierra Sheard Kelly, Shelea, Raven Goodwin, Angela Birchett, Kierra Sheard", "Drama", "7.5")
)

print("***** Movie Listings *****")

while True:
    command = input("(L)ist all movies, get movie (D)etails, or (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command == "l":
        for movie in movie_list:
            movie.display_movie()
    elif command == "d":
        title = input("Enter movie name: ")
        for movie in movie_list:
            if movie.is_match(title):
                movie.display_movie()
            else:
                print("Sorry. We don't seem to have that movie in our listing.")
    else:
        print("Invalid Command.")
            
print("Goodbye.")