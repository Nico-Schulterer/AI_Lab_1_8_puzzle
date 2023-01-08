import copy
import sys
import PuzzleBasicFunctions as nodeCreator
from queue import PriorityQueue

def solveRandomPuzzle():
    # Create a random start node
    startNode = nodeCreator.createShuffledParentNode(1)
    nodeCreator.printNode(startNode)

    solveSpecificPuzzle(startNode)


def solveSpecificPuzzle(startNode):

    # Check if solvable otherwise stop immediately
    if nodeCreator.checkIfSolvable(startNode) == 0:
        return

    # Create an array for all created nodes and add the startNode
    allNodes = nodeCreator.NodePriorityQueue()

    # Create a node that holds the current iterated node
    currentNode = startNode

    index = 0
    # Loop until the heuristics of a node reach 0 thus deliver the desired result
    while currentNode.h > 0:

        index += 1

        print("Searching: g-cost = " + str(currentNode.g) + " | h-cost = " + str(currentNode.h) + " | f-cost = " + str(currentNode.f))
        # nodeCreator.printNode(currentNode)
        # Create child nodes of the current node
        childNodes = nodeCreator.createChildNodes(currentNode)

        # Add the child nodes to the list with all Nodes
        for node in childNodes:
            allNodes.put(node, node.f)

        # Sort array with all nodes by their cost f(n)
        # allNodes.sort(key=lambda x: x.f)

        # Pick the next node with the least cost that hasn't been visited yet
        currentNode = allNodes.get()

    # Print path of all nodes to solve the puzzle
    print("\nFinished Puzzle: g-cost/depth = " + str(currentNode.g) + " | total iterations: " + str(index) + "\n")
    nodeCreator.printAllNodes(currentNode)


if __name__ == '__main__':
    startNode = nodeCreator.Node()
    startNode.puzzleField[0][0] = 2
    startNode.puzzleField[0][1] = 0
    startNode.puzzleField[0][2] = 5
    startNode.puzzleField[1][0] = 1
    startNode.puzzleField[1][1] = 8
    startNode.puzzleField[1][2] = 7
    startNode.puzzleField[2][0] = 3
    startNode.puzzleField[2][1] = 6
    startNode.puzzleField[2][2] = 4

    startNode.heuristicApproach = 1
    nodeCreator.calculateManhatten(startNode)

    # solveSpecificPuzzle(startNode)
    solveRandomPuzzle()
    #testNode = nodeCreator.Node()
    #testNode.puzzleField = copy.deepcopy(startNode.puzzleField)

    #print(comparePuzzles(testNode, startNode))

    # n1 = nodeCreator.createShuffledParentNode(1)
    # n2 = nodeCreator.createShuffledParentNode(1)
    # n3 = nodeCreator.createShuffledParentNode(1)
    # n4 = nodeCreator.createShuffledParentNode(1)
    # n5 = nodeCreator.createShuffledParentNode(1)
    # n6 = nodeCreator.createShuffledParentNode(1)

    # print(n1.h)
    # print(n2.h)
    # print(n3.h)
    # print(n4.h)
    # print(n5.h)
    # print(n6.h)

    # q = nodeCreator.NodePriorityQueue()

    # q.put(n1, n1.h)
    # q.put(n2, n2.h)
    # q.put(n3, n3.h)

    # print("Dequeued Node:")
    # nodeX = q.get()
    # print(nodeX.h)



