import fresh_tomatoes
import media

# Creating a object
batman = media.Movie("THe Dark Knight Rises", "A real hero",
 "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg", # noqa
 "https://www.youtube.com/watch?v=GokKUqLcvD8")
# Creating a object
superman_batman = media.Movie("Superman vs Batman", "God vs Man",
 "https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg", # noqa
 "https://www.youtube.com/watch?v=eX_iASz1Si8")
# Creating a object
captain_america = media.Movie("Captain America", "The Friendship",
 "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg", # noqa
 "https://www.youtube.com/watch?v=dKrVegVI0Us")
# Creating a object
jurassic = media.Movie("Jurassic World", "The dinosaurs",
 "https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg", # noqa
 "https://www.youtube.com/watch?v=RFinNxS5KN4")
# Creating a object
insterstellar = media.Movie("Interstellar", "A Father, and a Journey Back",
 "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", # noqa
 "https://www.youtube.com/watch?v=zSWdZVtXT7E")

movies = [batman, superman_batman, captain_america, jurassic, insterstellar]
# Calling open_movies_page function from fresh_tomatoes file
fresh_tomatoes.open_movies_page(movies)

