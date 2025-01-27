# region imports

import Die

# endregion

# region function declarations
def main():
    """
    This function rolls a fair die 1000 times and tallies the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores = [0,0,0,0,0,0]  # create a list with 6 elements/items initialized to 0's
    n = 1000  # how many times to roll the die
    for i in range(n):  # each time through the loop, roll die and increment a score
        score = Die.rollFairDie()  # score = 1 to 6
        scores[(score-1)] += 1  # increment score-1 item b/c 0 indexing start
    prob = [0,0,0,0,0,0]
    for j in range(0,6,1):
        prob[j] =  (scores[j] / n)
    # print the result
    print("The total number of scores after rolling a fair die", n, "times is:")
    print(scores)
    print("the probabilities of this outcome:")
    print(prob)


def main2():
    """
    This function rolls a fair die 10000 times and tallys the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores2 = [0, 0, 0, 0, 0, 0]  # create a list with 6 elements/items initialized to 0's
    n2 = 10000  # how many times to roll the die
    for i in range(n2):  # each time through the loop, roll die and increment a score
        score2 = Die.rollFairDie()  # score = 1 to 6
        scores2[(score2 - 1)] += 1  # increment score-1 item b/c 0 indexing start
    prob2 = [0, 0, 0, 0, 0, 0]
    for j in range(0, 6, 1):
        prob2[j] = (scores2[j] / n2)
    # print the result
    print("The total number of scores after rolling a fair die", n2, "times is:")
    print(scores2)
    print("the probabilities of this outcome:")
    print(prob2)

    pass


def main3():
    """
    This function rolls an unfair die 10000 times and tallys the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores3 = [0, 0, 0, 0, 0, 0]  # create a list with 6 elements/items initialized to 0's
    n3 = 10000  # how many times to roll the die
    for i in range(n3):  # each time through the loop, roll die and increment a score
        score3 = Die.rollUnFairDie()  # score = 1 to 6
        scores3[(score3 - 1)] += 1  # increment score-1 item b/c 0 indexing start
    prob3 = [0, 0, 0, 0, 0, 0]
    for j in range(0, 6, 1):
        prob3[j] = (scores3[j] / n3)
    # print the result
    print("The total number of scores after rolling an unfair die", n3, "times is:")
    print(scores3)
    print("the probabilities of this outcome:")
    print(prob3)


pass


# endregion

# this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    print()
    main2()
    print()
    main3()
