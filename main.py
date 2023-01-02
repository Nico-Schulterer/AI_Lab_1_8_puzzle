import CreateRandomPuzzle as nodeCreator
import math

if __name__ == '__main__':

    n1 = nodeCreator.createShuffledNode()
    nodeCreator.printNode(n1)
    n1.h = nodeCreator.calculateManhatten(n1)
    print(n1.h)

    x = abs(0 - (math.floor(1 / 3)))
    print("X = " + str(x))

