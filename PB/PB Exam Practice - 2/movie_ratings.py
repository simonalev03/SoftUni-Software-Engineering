# Read input
number_of_films = int(input())
# Logic
highest_rating = 0
lowest_rating = float('inf') # I dont understand this
avg_rating = 0
all_films_rating = 0
highest_ranked_film = ""
lowest_ranked_film = ""
for film in range(number_of_films):
    film_name = input()
    film_rating = float(input())
    all_films_rating += film_rating
    if film_rating > highest_rating:
        highest_rating = film_rating
        highest_ranked_film = film_name
    elif film_rating < lowest_rating:
        lowest_rating = film_rating
        lowest_ranked_film = film_name
avg_rating = all_films_rating / number_of_films
# Print output
print(f"{highest_ranked_film} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_ranked_film} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {avg_rating:.1f}")
