import fresh_tomatoes
import media
# importing fresh_tomatoes module and media module

""" This is Deb's favourite movie trailer website """

# Created multiple variable indexs for the movies list array
movie1 = media.Movie("3 Idiots",
 "2 friends form a great bond with Rancho due to his refreshing outlook.....",
 "images/three_idiots.jpg",
 "https://www.youtube.com/watch?v=xvszmNXdM4w")
movie2 = media.Movie("Finding Nemo",
 "After his son gets abducted in the Great Barrier Reef........",
 "images/Finding Nemo.jpeg",
 "https://www.youtube.com/watch?v=2zLkasScy7A")
movie3 = media.Movie("Baahubali",
 "In the kingdom of Mahishmati, while pursuing his love, Shivudu.........",
 "images/Bahubali.jpg",
 "https://www.youtube.com/watch?v=VdafjyFK3ko")
movie4 = media.Movie("Toy Story",
 """Andy's favourite toy, Woody, is worried as Andy receives his gift,
 a new toy called............""",
 "images/toy_story.jpg",
 "https://www.youtube.com/watch?v=KYz2wyBy3kc")
movie5 = media.Movie("Avatar",
 """Jake, a paraplegic marine, replaces his brother on the Na'vi inhabited
 Pandora for a corporate mission...........""",
 "images/avatar.jpg",
 "https://www.youtube.com/watch?v=5PSNL1qE6VY")
movie6 = media.Movie("School Of Rock",
 """Dewey Finn, an amateur rock enthusiast, slyly takes up his friend's
 substitute teacher's job..........""",
 "images/School_of_Rock.jpg",
 "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# The movie list array
movies = [movie1, movie2, movie3, movie4, movie5, movie6]

# function trigger to open_movies_page function with movie array
fresh_tomatoes.open_movies_page(movies)
