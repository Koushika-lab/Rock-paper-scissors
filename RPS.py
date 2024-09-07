# Helper function to counter the predicted move
import random
def get_counter_move(move):
    if move == "R":
        return "P"  # Paper beats Rock
    elif move == "P":
        return "S"  # Scissors beats Paper
    else:
        return "R"  # Rock beats Scissors

def player(prev_play, opponent_history=[], play_order={}):
    # Store the opponent's moves
    if prev_play:
        opponent_history.append(prev_play)

    # Default to "R" if no history exists
    if len(opponent_history) == 0:
        return "R"

    # Frequency-based strategy (track the most frequent opponent moves)
    if len(opponent_history) < 5:
        # For the first few moves, return random or fixed
        return random.choice(["R", "P", "S"])
    
    # Analyze the last 3-move sequence to detect patterns
    last_three = "".join(opponent_history[-3:])
    last_two = "".join(opponent_history[-2:])

    if last_three in play_order:
        play_order[last_three] += 1
    else:
        play_order[last_three] = 1

    if last_two in play_order:
        play_order[last_two] += 1
    else:
        play_order[last_two] = 1

    # Use the most frequent pattern to predict the opponent's next move
    if play_order:
        if last_three in play_order and play_order[last_three] > play_order[last_two]:
            predict = last_three[-1]
        else:
            predict = last_two[-1]
    else:
        predict = random.choice(["R", "P", "S"])

    # Counter the predicted move
    guess = get_counter_move(predict)

    return guess