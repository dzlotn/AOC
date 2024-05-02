def is_possible(game_info, cube_counts):
    for subset in game_info:
        cubes = subset.split()
        color = cubes[1]  # Extract the color
        count = int(cubes[0])  # Extract the count
        # Remove the comma from the color if present
        if color.endswith(','):
            color = color[:-1]
        if cube_counts[color] < count:
            return False
    return True

def possible_games(records, cube_counts):
    possible = []
    for game in records:
        game_id, info = game.split(": ")
        game_info = info.split("; ")
        if is_possible(game_info, cube_counts):
            possible.append(int(game_id.split()[1]))
    return possible
# Puzzle input
records = open("AOC2/input2.txt","r")

cube_counts = {
    "red": 12,
    "green": 13,
    "blue": 14
}

possible = possible_games(records, cube_counts)
print("The IDs of the possible games are:", possible)
print("The sum of their IDs is:", sum(possible))
