import math
import copy
import numpy as np


# A node class that contains the state of a puzzle field and its current cost
class Node:
    puzzleField = np.arange(9).reshape(3, 3)
    g = 0
    h = 0
    f = 0
    parentNode = 0
    heuristicApproach = 0  # 0 = hamming, 1 = manhatten


# Counts the amount of inversion in the node
def checkInversionCount(node):
    count = 0
    empty = 0
    arr = node.flatten()

    for x in arr - 1:
        if arr[x] > arr[x + 1] and arr[x] != empty:
            count += 1
    print(count)
    return count


# Checks if the node is solvable based on the amount of inversions
def checkIfSolvable(node):
    count = checkInversionCount(node.puzzleField)
    if count % 2 == 0:
        print("This node is solvable!")
        return 1
    else:
        print("This node is not solvable!")
        return 0


# Calculates the heuristics h(n) of the hamming distances of each value on the field and the overall cost f(n)
def calculateHamming(node):
    counter = 0
    heuristic = 0
    for x in range(3):
        for y in range(3):
            if counter != node.puzzleField[x][y]:
                heuristic += 1
            counter += 1
    node.h = heuristic
    node.f = node.g + node.g


# Calculates the heuristics h(n) of the manhatten distances of each value on the field and the overall cost f(n)
def calculateManhatten(node):
    heuristic = 0
    for x in range(3):
        for y in range(3):
            v1 = abs(y - (node.puzzleField[x][y] % 3))
            v2 = abs(x - (math.floor(node.puzzleField[x][y] / 3)))
            h = v1 + v2
            heuristic += h
    node.h = heuristic
    node.f = node.g + node.h


# Returns a new random shuffled node
def createShuffledParentNode(heuristicApproach):
    # Create new node
    node = Node()

    # Create random 2d puzzle field
    randomPuzzle = np.arange(9)
    np.random.shuffle(randomPuzzle)
    node.puzzleField = np.reshape(randomPuzzle, (3,3))

    # Define approach of heuristics and retr
    node.heuristicApproach = heuristicApproach

    # Return manhatten approach
    if node.heuristicApproach == 1:
        calculateManhatten(node)
        return node

    # Return default (hamming) approach
    calculateHamming(node)
    return node


# Returns a new copy of an existing node and changes its puzzle field
def createChildFromParent(parentNode, xParent, yParent, xValue, yValue):
    # Create a copy
    node = copy.copy(parentNode)

    # Increase tree depth cost
    node.g += 1

    # Define parent node
    node.parentNode = parentNode

    # Swap empty value in the puzzle field
    node.puzzleField[xParent][yParent] = node.puzzleField[xParent + xValue][yParent + yValue]
    node.puzzleField[xParent + xValue][yParent + yValue] = 0

    # Return manhatten approach
    if node.heuristicApproach == 1:
        calculateManhatten(node)
        return node

    # Return default (hamming) approach
    calculateHamming(node)
    return node


# Returns an array of child nodes created from a single parent node
def createChildNodes(parentNode):
    # Create array of child nodes
    childNodes = []

    # Find the position of the empty value in the puzzle field
    xAxis = yAxis = 0

    for x in range(3):
        for y in range(3):
            if parentNode.puzzleField[x][y] == 0:
                xAxis = x
                yAxis = y
                break

    # Find the neighbors of the empty value in the puzzle field and create new child nodes
    if xAxis - 1 >= 0:  # left
        childNodeLeft = createChildFromParent(parentNode, xAxis, yAxis, -1, 0)
        childNodes.append(childNodeLeft)

    if xAxis + 1 < 3:  # right
        childNodeRight = createChildFromParent(parentNode, xAxis, yAxis, 1, 0)
        childNodes.append(childNodeRight)

    if yAxis - 1 >= 0:  # bottom
        childNodeBottom = createChildFromParent(parentNode, xAxis, yAxis, 0, -1)
        childNodes.append(childNodeBottom)

    if yAxis + 1 < 3:  # top
        childNodeTop = createChildFromParent(parentNode, xAxis, yAxis, 0, 1)
        childNodes.append(childNodeTop)

    # Return child nodes
    return childNodes


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
