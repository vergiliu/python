import random


class Node:
    data = None
    left = None
    right = None

    def __init__(self, initial_value):
        self.data = initial_value

    def add_node(self, new_node):
        if not self:
            self = new_node
        elif new_node.data >= self.data:
            if not self.right:
                self.right = new_node
            else:
                self.right.add_node(new_node)
        else:
            if not self.left:
                self.left = new_node
            else:
                self.left.add_node(new_node)

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        if self:
            print str(self.data),
        if self.right:
            self.right.print_in_order()

    def check_in_order(self, mini, maxi):
        if self.left:
            self.left.check_in_order(mini, maxi)
        if self:
            print str("data= {} min={} max={}=> {}/{}".format(self.data))
        if self.right:
            self.right.check_in_order(mini, maxi)


if __name__ == "__main__":

    root = Node(0)

    for i in range(1, 10):
        value = random.randint(1, 1000)
        root.add_node(Node(value))
        print value,

    root.print_in_order()
    root.check_in_order(0, 0)

    print "\n---"

    broken = Node(3)
    broken.left = Node(2)
    broken.left.left = Node(1)
    broken.left.right = Node(4)
    broken.right = Node(5)
    broken.right.left = Node(6)

    broken.print_in_order()
    broken.check_in_order(3, 3)
