import PuzzleBasicFunctions as nodeCreator


def solveRandomPuzzle():

    # Create a random start node
    startNode = nodeCreator.createShuffledParentNode(1)

    # Solve node
    return solveSpecificPuzzle(startNode)


def solveSpecificPuzzle(startNode):

    # Check if solvable otherwise stop immediately
    if nodeCreator.checkIfSolvable(startNode) == 0:
        return

    # Create a priority queue for all created nodes
    allNodes = nodeCreator.NodePriorityQueue()

    # Create array for all visited nodes
    visitedNodes = []

    # Create a node that holds the current iterated node
    allNodes.put(startNode, startNode.f)

    # Data Stats
    iterations = 0
    numberOfNodes = 1

    # Loop until the heuristics of a node reach 0 thus deliver the desired result
    while not allNodes.empty():

        # Get current node of priority queue
        currentNode = allNodes.get()

        # Check for repetition
        if currentNode.puzzleField in visitedNodes:
            continue

        # Stop the loop when heuristic od current node reaches 0
        if currentNode.h == 0:
            break

        # Add puzzle field of current node to visited nodes
        visitedNodes.append(currentNode.puzzleField)

        # Print current node stats
        iterations += 1
        print("Searching: g-cost = " + str(currentNode.g) + " | h-cost = " + str(currentNode.h) + " | f-cost = " + str(currentNode.f))

        # Create child nodes of the current node
        childNodes = nodeCreator.createChildNodes(currentNode)

        # Add the child nodes to the list with all Nodes
        for node in childNodes:
            allNodes.put(node, node.f)
            numberOfNodes += 1

    # Print path of all nodes to solve the puzzle
    print("\nFinished Puzzle: g-cost/depth = " + str(currentNode.g) +
          " | total iterations = " + str(iterations) +
          " | number of nodes = " + str(numberOfNodes) + "\n")

    return currentNode


if __name__ == '__main__':
    startNode = nodeCreator.Node()
    startNode.puzzleField[0][0] = 2
    startNode.puzzleField[0][1] = 6
    startNode.puzzleField[0][2] = 0
    startNode.puzzleField[1][0] = 1
    startNode.puzzleField[1][1] = 8
    startNode.puzzleField[1][2] = 7
    startNode.puzzleField[2][0] = 3
    startNode.puzzleField[2][1] = 4
    startNode.puzzleField[2][2] = 5

    startNode.heuristicApproach = 1
    nodeCreator.calculateManhatten(startNode)

    # solveSpecificPuzzle(startNode)
    solveRandomPuzzle()



