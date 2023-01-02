import math
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


# Returns the sum of all calculated hamming distances of each value on the field
def calculateHamming(node):
    counter = 0
    heuristic = 0
    for x in range(3):
        for y in range(3):
            if counter != node.puzzleField[x][y]:
                heuristic += 1
            counter += 1
    return heuristic


# Returns the sum of all calculated manhatten distances of each value on the field
def calculateManhatten(node):
    heuristic = 0
    for x in range(3):
        for y in range(3):
            v1 = abs(y - (node.puzzleField[x][y] % 3))
            v2 = abs(x - (math.floor(node.puzzleField[x][y] / 3)))
            h = v1 + v2
            heuristic += h
    return heuristic


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
