import fresh_tomatoes
import media

three_idiots = media.Movie("3 Idiots", "In college, Farhan and Raju form a great bond with Rancho due to his refreshing outlook. Years later, a bet gives them a chance to look for their long-lost friend whose existence seems rather elusive.", "http://www.gstatic.com/tv/thumb/movieposters/7951929/p7951929_p_v8_aa.jpg", "https://www.youtube.com/watch?v=xvszmNXdM4w")
finding_nemo = media.Movie("Finding Nemo", "After his son gets abducted in the Great Barrier Reef and is despatched to Sydney, a meek clownfish embarks on a journey to bring him home.", "https://d35fkdjhhgt99.cloudfront.net/static/use-media-items/17/16315/full-1028x1500/56702cc2/Finding%20Nemo%20%282003%29%202.jpeg?resolution=0", "https://www.youtube.com/watch?v=2zLkasScy7A")
baahubali = media.Movie("Baahubali", "In the kingdom of Mahishmati, while pursuing his love, Shivudu learns about the conflict-ridden past of his family and his legacy. He must now prepare himself to face his new-found archenemy.", "http://4.bp.blogspot.com/-ESdMlxdjmfs/VZ3xhEtQUSI/AAAAAAAAjUs/w4EybAdIIoc/s1600/Bahubali%2BHD%2BWallpaperes%2B7.jpg", "https://www.youtube.com/watch?v=VdafjyFK3ko")

toy_story = media.Movie("Toy Story", "Andy's favourite toy, Woody, is worried that after Andy receives his birthday gift, a new toy called Buzz Lightyear, his importance may get reduced. He thus hatches a plan to eliminate Buzz.", "http://www.impawards.com/1995/posters/toy_story_ver1.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "Jake, a paraplegic marine, replaces his brother on the Na'vi inhabited Pandora for a corporate mission. He is accepted by the natives as one of their own but he must decide where his loyalties lie.", "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
school_of_rock = media.Movie("School Of Rock", "Dewey Finn, an amateur rock enthusiast, slyly takes up his friend's substitute teacher's job. Bearing no qualifications for it, he instead starts training the students to be a bandself.", "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

movies = [three_idiots, finding_nemo, baahubali, toy_story, avatar, school_of_rock]
fresh_tomatoes.open_movies_page(movies)
