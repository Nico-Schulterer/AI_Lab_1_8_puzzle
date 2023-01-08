import copy
import time
import PuzzleBasicFunctions as nodeCreator


def solveRandomPuzzle(heuristicApproach):

    # Create a random start node
    startNode = nodeCreator.createShuffledParentNode(heuristicApproach)

    # Solve node
    return solveSpecificPuzzle(startNode)


def solveSpecificPuzzle(startNode):
    nodeCreator.printNode(startNode)

    # Data Stats
    computationTime = time.time()
    iterations = 0
    numberOfNodes = 1

    # Check if solvable otherwise stop immediately
    if nodeCreator.checkIfSolvable(startNode) == 0:
        return 0, 0, 0

    # Create a priority queue for all created nodes
    allNodes = nodeCreator.NodePriorityQueue()

    # Create array for all visited nodes
    visitedNodes = []

    # Create a node that holds the current iterated node
    allNodes.put(startNode, startNode.f)

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

    # Data Stats
    computationTime = time.time() - computationTime

    return currentNode, computationTime, numberOfNodes


def compareHeuristics():
    # Manhatten
    manhattenNodes = 0
    manhattenTime = 0

    # Hamming
    hammingNodes = 0
    hammingTime = 0

    # Search 100 times
    for i in range(10):

        startNode = nodeCreator.createShuffledParentNode(0)

        endNode, time, nodes = solveSpecificPuzzle(startNode)
        manhattenTime += time
        manhattenNodes += nodes

        startNode.heuristicApproach = 0
        nodeCreator.calculateHamming(startNode)
        endNode, time, nodes = solveSpecificPuzzle(startNode)
        hammingTime += time
        hammingNodes += nodes


    # Print data
    print("\nManhatten Heuristic for 100 searches: time = " + str(manhattenTime) + " nodes = " + str(manhattenNodes))
    print("\nHamming Heuristic for 100 searches: time = " + str(hammingTime) + " nodes = " + str(hammingNodes))


if __name__ == '__main__':

    # Solve specific puzzle
    """
    startNode = nodeCreator.Node()
    startNode.puzzleField = [[2, 6, 0], [1, 8, 7], [3, 4, 5]]
    startNode.heuristicApproach = 1
    endNode, time, nodes = solveSpecificPuzzle(startNode)
    nodeCreator.printAllNodes(endNode)
    print("Computation Time: " + str(time))
    print("Number of nodes: " + str(nodes))
    
    endNode, time, nodes = solveRandomPuzzle()
    nodeCreator.printAllNodes(endNode)
    print(time)
    print(nodes)
    """

    # Solve random puzzle
    endNode, time, nodes = solveRandomPuzzle(1)
    nodeCreator.printAllNodes(endNode)
    print("Computation Time: " + str(time))
    print("Number of Nodes: " + str(nodes))

    # Compare heuristics
    """
    # compareHeuristics()
    """
