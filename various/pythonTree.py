
import random

class Node:

    data = None
    left =  None
    right = None

    def __init__(self, initialValue):
        self.data = initialValue

    def addNode(self, newNode):
        if not self:
            self = newNode
        elif newNode.data >= self.data:
            if not self.right:
                self.right = newNode
            else:
                self.right.addNode(newNode)
        else:
            if not self.left:
                self.left = newNode
            else:
                self.left.addNode(newNode)

    def printInorder(self):
        if self.left:
            self.left.printInorder()
        if self:
            print str(self.data),
        if self.right:
            self.right.printInorder()

if __name__ == "__main__":

    root = Node(0)

    for i in xrange(1,100):
        value = random.randint(1,1000)
        root.addNode(Node(value))
        print value,

    print "\n---"

    root.printInorder()

