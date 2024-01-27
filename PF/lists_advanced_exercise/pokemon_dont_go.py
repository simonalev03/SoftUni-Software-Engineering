distances_of_pokemon = [int(distance) for distance in input().split()]
copied_distances = distances_of_pokemon.copy()
for current_pokemon_index in range(len(distances_of_pokemon)):
    pokemon_index = int(input())
    captured_pokemon = copied_distances.pop(pokemon_index)
    for current_distance in distances_of_pokemon:
        if current_distance >= captured_pokemon:
            distances_of_pokemon[current_pokemon_index] += distances_of_pokemon[captured_pokemon]
            print(distances_of_pokemon)


