# region imports
import Die
# endregion

# region functions
def rollDice(N=1):
    """
    This function simulates rolling N dice simultaneously by using a loop that rolls
    a single die N times and totaling the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
    #JES MISSING CODE
    total = 0
    if N > 1:
        for i in range(N):
            face = Die.rollFairDie()
            total = total + face
    else:
        total = total + Die.rollFairDie()

    print(total)
    pass

def rollUnFairDice(N=1):
    """
    This function simulates rolling N, UnFair dice simultaneously by using a loop that rolls
    a single die N times and totals the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
    #JES MISSING CODE
    pass

# endregion

# this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    rollDice()