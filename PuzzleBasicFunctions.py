import math
import copy
from queue import PriorityQueue
import random

# A node class that contains the state of a puzzle field and its current cost
class Node():
    puzzleField = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    g = 0
    h = 0
    f = 0
    parentNode = 0
    heuristicApproach = 0  # 0 = hamming, 1 = manhatten


# Create a priority queue for node objects
class NodePriorityQueue(PriorityQueue):

    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item


# Counts the amount of inversion in the node version 2
def checkInversionCount2(puzzleField):
    count = 0
    arr = [j for sub in puzzleField for j in sub]

    for x in range(len(arr) - 1):
        for i in range(x, len(arr)):
            if arr[x] > arr[i] != 0:
                count += 1
    print("Inversion Count: " + str(count))
    return count


# Checks if the node is solvable based on the amount of inversions
def checkIfSolvable(node):
    count = checkInversionCount2(node.puzzleField)
    if count % 2 == 0:
        print("This node is solvable! \n")
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
    node.f = node.g + node.h


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

    while True:
        # Create new node
        nodeX = Node()

        # Create random 2d puzzle field
        random.shuffle(nodeX.puzzleField)
        for i in nodeX.puzzleField:
            random.shuffle(i)

        # Check solvability
        if checkIfSolvable(nodeX) == 1:
            break

    # Define approach of heuristics
    nodeX.heuristicApproach = heuristicApproach

    # Return manhatten approach
    if nodeX.heuristicApproach == 1:
        calculateManhatten(nodeX)
        return nodeX

    # Return default (hamming) approach
    calculateHamming(nodeX)
    return nodeX


# Returns a new copy of an existing node and changes its puzzle field
def createChildFromParent(parentNode, xParent, yParent, xValue, yValue):
    # Create a copy
    node = Node()
    puzzleField = parentNode.puzzleField
    node.puzzleField = copy.deepcopy(puzzleField)

    # Swap empty value in the puzzle field
    node.puzzleField[xParent][yParent] = node.puzzleField[xParent + xValue][yParent + yValue]
    node.puzzleField[xParent + xValue][yParent + yValue] = 0

    # Check if node is not a copy of a parent node to prevent loops
    if checkLoops(node) == 0:
        return 0

    # Increase tree depth cost
    node.g = copy.deepcopy(parentNode.g) + 1
    node.heuristicApproach = copy.deepcopy(parentNode.heuristicApproach)

    # Define parent node
    node.parentNode = parentNode

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
    if yAxis - 1 >= 0:  # left
        childNodeBottom = createChildFromParent(parentNode, xAxis, yAxis, 0, -1)
        if childNodeBottom != 0:
            childNodes.append(childNodeBottom)

    if xAxis - 1 >= 0:  # top
        childNodeLeft = createChildFromParent(parentNode, xAxis, yAxis, -1, 0)
        if childNodeLeft != 0:
            childNodes.append(childNodeLeft)

    if yAxis + 1 < 3:  # right
        childNodeTop = createChildFromParent(parentNode, xAxis, yAxis, 0, 1)
        if childNodeTop != 0:
            childNodes.append(childNodeTop)

    if xAxis + 1 < 3:  # bottom
        childNodeRight = createChildFromParent(parentNode, xAxis, yAxis, 1, 0)
        if childNodeRight != 0:
            childNodes.append(childNodeRight)

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


def printAllNodes(endNode):
    nodePath = [endNode]
    currentNode = endNode

    while currentNode.parentNode != 0:
        currentNode = currentNode.parentNode
        nodePath.append(currentNode)

    nodePath.reverse()

    for i in range(len(nodePath)):
        print("Step: " + str(i + 1))
        printNode(nodePath[i])


def comparePuzzles(node1, node2):
    for x in range(3):
        for y in range(3):
            if node1.puzzleField[x][y] != node2.puzzleField[x][y]:
                return 0
    return 1


def checkLoops(node):
    parentNode = node.parentNode
    while parentNode != 0:
        if comparePuzzles(node, parentNode) == 1:
            return 0
        parentNode = parentNode.parentNode
    return 1
