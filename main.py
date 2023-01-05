import sys
import PuzzleBasicFunctions as nodeCreator


def solveRandomPuzzle():
    # Create a random start node
    startNode = nodeCreator.createShuffledParentNode(1)

    solveSpecificPuzzle(startNode)


def solveSpecificPuzzle(startNode):

    # Check if solvable otherwise stop immediately
    if nodeCreator.checkIfSolvable(startNode) == 0:
        return

    # Create an array for all created nodes and add the startNode
    allNodes = [startNode]

    # Create a node that holds the current iterated node
    currentNode = startNode

    index = 0
    # Loop until the heuristics of a node reach 0 thus deliver the desired result
    while currentNode.h > 0:

        index += 1

        print("g - cost: " + str(currentNode.g) + " | h - cost: " + str(currentNode.h) + " | f - cost: " + str(currentNode.f))
        nodeCreator.printNode(currentNode)
        # Create child nodes of the current node
        childNodes = nodeCreator.createChildNodes(currentNode)

        # Add the child nodes to the list with all Nodes
        for node in childNodes:
            allNodes.append(node)

        # Sort array with all nodes by their cost f(n)
        # allNodes.sort(key=lambda x: x.f)

        # Pick the next node with the least cost that hasn't been visited yet
        cheapestNode = sys.maxsize

        for node in allNodes:
            if node.f < cheapestNode and node.hasBeenVisited == 0:
                currentNode = node
                cheapestNode = currentNode.f

    print("Finished Puzzle: " + str(currentNode.g) + " | Iterations: " + str(index))
    nodeCreator.printNode(currentNode)


def testing():
    testNode = nodeCreator.createShuffledParentNode(0)

    nodeCreator.printNode(testNode)
    print("childNodes: ----------------------------------------------------------")

    childNodes = nodeCreator.createChildNodes(testNode)

    for node in childNodes:
        nodeCreator.printNode(node)

    print("parentNode: ----------------------------------------------------------")
    nodeCreator.printNode(testNode)


if __name__ == '__main__':
    startNode = nodeCreator.Node()
    startNode.puzzleField[0][0] = 3
    startNode.puzzleField[0][1] = 1
    startNode.puzzleField[0][2] = 5
    startNode.puzzleField[1][0] = 6
    startNode.puzzleField[1][1] = 7
    startNode.puzzleField[1][2] = 0
    startNode.puzzleField[2][0] = 8
    startNode.puzzleField[2][1] = 2
    startNode.puzzleField[2][2] = 4

    startNode.heuristicApproach = 1
    nodeCreator.calculateManhatten(startNode)
    # print(startNode.h)
    nodeCreator.printNode(startNode)

    # nodeCreator.checkInversionCount(startNode.puzzleField)
    # nodeCreator.checkInversionCount2(startNode.puzzleField)

    # childNodes = nodeCreator.createChildNodes(startNode)
    # childNodes2 = nodeCreator.createChildNodes(childNodes[0])
    # childNodes3 = nodeCreator.createChildNodes(childNodes2[0])

    # solveSpecificPuzzle(startNode)
    solveRandomPuzzle()

