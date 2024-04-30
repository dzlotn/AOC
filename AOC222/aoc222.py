# Define the rules
rules = {
    "A": "X",  # Rock beats Scissors
    "B": "Y",  # Paper beats Rock
    "C": "Z"   # Scissors beat Paper
}

# Function to determine the result of a single game
def game(player1, player2):
    if player1 == player2:
        return "tie"
    elif rules[player1] == player2:
        return "win"
    else:
        return "lose"

# Read the game data from file
with open("AOC222/aoc222.txt", "r") as file:
    total_score = 0
    for line in file:
        players = line.split()
        result = game(players[0], players[1])
        if result == "win":
            total_score += 1
        elif result == "tie":
            total_score += 3  # Ties give 3 points as per your code
        # Losing doesn't affect the score

print("Total score:", total_score)
