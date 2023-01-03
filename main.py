import numpy as np
import PuzzleBasicFunctions as nodeCreator
import copy


def solvePuzzle(startNode):
    if nodeCreator.checkIfSolvable(startNode) == 0:
        return

    startNode.h = nodeCreator.calculateHamming(startNode)
    startNode.g = 0
    startNode.f = startNode.h + startNode.g

    allNodes = [startNode]
    index = 0

    while allNodes[0].h > 0:
        index += 1
        print(str(index) + ": " + str(allNodes[0].h))
        # Find x and y axis of 0
        xAxis = yAxis = 0

        for x in range(3):
            for y in range(3):
                if allNodes[0].puzzleField[x][y] == 0:
                    xAxis = x
                    yAxis = y

        # Find neighbors of 0 and create new nodes with changed values in the puzzle field
        if xAxis - 1 >= 0:
            childNode = copy.copy(allNodes[0])
            childNode.puzzleField[xAxis, yAxis] = childNode.puzzleField[xAxis - 1, yAxis]
            childNode.puzzleField[xAxis - 1, yAxis] = 0
            childNode.h = nodeCreator.calculateHamming(childNode)
            childNode.g += 1
            childNode.f = childNode.h + childNode.g
            childNode.startNode = allNodes[0]
            allNodes.append(childNode)

        if xAxis + 1 < 3:
            childNode = copy.copy(allNodes[0])
            childNode.puzzleField[xAxis, yAxis] = childNode.puzzleField[xAxis + 1, yAxis]
            childNode.puzzleField[xAxis + 1, yAxis] = 0
            childNode.h = nodeCreator.calculateHamming(childNode)
            childNode.g += 1
            childNode.f = childNode.h + childNode.g
            childNode.startNode = allNodes[0]
            allNodes.append(childNode)

        if yAxis - 1 >= 0:
            childNode = copy.copy(allNodes[0])
            childNode.puzzleField[xAxis, yAxis] = childNode.puzzleField[xAxis, yAxis - 1]
            childNode.puzzleField[xAxis, yAxis - 1] = 0
            childNode.h = nodeCreator.calculateHamming(childNode)
            childNode.g += 1
            childNode.f = childNode.h + childNode.g
            childNode.startNode = allNodes[0]
            allNodes.append(childNode)

        if yAxis + 1 < 3:
            childNode = copy.copy(allNodes[0])
            childNode.puzzleField[xAxis, yAxis] = childNode.puzzleField[xAxis, yAxis + 1]
            childNode.puzzleField[xAxis, yAxis + 1] = 0
            childNode.h = nodeCreator.calculateHamming(childNode)
            childNode.g += 1
            childNode.f = childNode.h + childNode.g
            childNode.startNode = allNodes[0]
            allNodes.append(childNode)

        # Sort nodes by their cost f(n)
        allNodes.sort(key=lambda x: x.f)

    print(nodeCreator.printNode(allNodes[0]))

if __name__ == '__main__':

    # Create random puzzle
    newNode = nodeCreator.createShuffledNode()

    # Print the initiate puzzle state
    nodeCreator.printNode(newNode)

    # Solve the puzzle
    solvePuzzle(newNode)


