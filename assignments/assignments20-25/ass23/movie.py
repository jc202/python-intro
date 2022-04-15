#Author: Justin C
class Movie:
    def __init__(self, title, description, actors, genre, rating):
        self.title = title
        self.description = description
        self.actors = (actors)
        self.genre = genre
        self.rating = float(rating)
    
    def display_movie(self):
        print(f"""
            *** {self.title} ***
            {self.description}
            Stars:
            - {self.actors}
            Genre: {self.genre}
            Rating: {self.rating}
            """)
    
    def is_match(self, title):
        if title == self.title:
            return True
        else:
            return False
