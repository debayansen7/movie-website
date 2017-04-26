import webbrowser
# using webbrowser module to connect url properties

class Movie():
    """ This is a movie class used to define and object that will contain all the necessary properties and methods for this class"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # __init__ is the contructor function used to define and create the object properties
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
