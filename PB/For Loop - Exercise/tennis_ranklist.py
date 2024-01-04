# Read user input
number_of_tournaments = int(input())
start_points = int(input())
total_points = 0
tournaments_won = 0
# Logic
for tournament in range(number_of_tournaments):
    tournament_placement = input()
    if tournament_placement == "W":
        total_points += 2000
        tournaments_won += 1
    elif tournament_placement == "F":
        total_points += 1200
    elif tournament_placement == "SF":
        total_points += 720

points_sum = total_points + start_points
avg_points_for_tournament = total_points / number_of_tournaments
percent_won_tournaments = tournaments_won / number_of_tournaments * 100
# Print output
print(f"Final points: {points_sum}")
print(f"Average points: {int(avg_points_for_tournament)}")
print(f"{percent_won_tournaments:.2f}%")