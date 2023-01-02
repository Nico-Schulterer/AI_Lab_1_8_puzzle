import numpy as np


# A node class that contains the state of a puzzle field and its current cost
class Node:
    puzzleField = np.arange(9).reshape(3, 3)
    g = 0
    h = 0
    f = 0


# Returns a random shuffled node
def createShuffledNode():
    n1 = Node()
    np.random.shuffle(n1.puzzleField.flat)
    return n1


# Prints the puzzle field of a node
def printNode(node):
    for x in range(3):
        for y in range(3):
            print("|", end=" ")
            print(node.puzzleField[x][y], end=" ")

        print("|")
        if x < 2:
            print("-------------")

    print("")
