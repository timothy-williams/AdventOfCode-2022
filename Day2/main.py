### ADVENT DAY 2 PART 1 ###

# -------RULES------- #

# A, X --> rock = 1 point
# B, Y --> paper = 2 points
# C, Z --> scissors = 3 points
# win = 6 points
# draw = 3 points
# loss = 0 points

outcomes = {
    'B X': 1, # loss, rock
    'C Y': 2, #       paper
    'A Z': 3, #       scissors
    'A X': 4, # draw, rock
    'B Y': 5, #       paper
    'C Z': 6, #       scissors
    'C X': 7, # win, rock
    'A Y': 8, #      paper
    'B Z': 9  #      scissors
}

def calculate_game_total():
    with open('D:\Github\AdventOfCode-2022\Day2\input.txt', 'r') as input_file:
        # create a list containing all rounds
        game_rounds = input_file.read().split('\n')

        # add points according to each round's result
        result = 0
        for round in game_rounds:
            for outcome in outcomes:
                if round == outcome:
                    result += outcomes[outcome]

        # total points earned     
        print(result)
    input_file.close()

calculate_game_total()

### PART 2 ###

# -------RULES------- #

# A --> rock = 1 point
# B --> paper = 2 points
# C --> scissors = 3 points
# X --> loss = 0 points
# Y --> draw = 3 points
# Z --> win = 6 points

outcomes = {
    'B X': 1, # loss, rock
    'C X': 2, #       paper
    'A X': 3, #       scissors
    'A Y': 4, # draw, rock
    'B Y': 5, #       paper
    'C Y': 6, #       scissors
    'C Z': 7, # win, rock
    'A Z': 8, #      paper
    'B Z': 9  #      scissors
}

calculate_game_total()