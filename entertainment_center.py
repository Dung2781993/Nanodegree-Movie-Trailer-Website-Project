import fresh_tomatoes
import media


dark_knight_rise = media.Movie("THe Dark Knight Rises",
						  	   "The world need a real hero",
						  	   "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
						  	   "https://www.youtube.com/watch?v=GokKUqLcvD8")

superman_and_batman = media.Movie("Superman vs Batman",
								  "God vs Man, Dark vs ",
								  "https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg",
								  "https://www.youtube.com/watch?v=eX_iASz1Si8")

captain_america = media.Movie("Captain America",
							  "The Borken Friendship",
							  "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
							  "https://www.youtube.com/watch?v=dKrVegVI0Us")

jurassic_world = media.Movie("Jurassic World",
							 "The game between dinosaurs",
							 "https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg",
							 "https://www.youtube.com/watch?v=RFinNxS5KN4")

insterstellar = media.Movie("Interstellar",
							"The story about a father's journey to see daughter",
							"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
							"https://www.youtube.com/watch?v=zSWdZVtXT7E")


movies = [dark_knight_rise,superman_and_batman,captain_america,jurassic_world,insterstellar]
fresh_tomatoes.open_movies_page(movies)

