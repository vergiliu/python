class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
    # todo - keep state
    # todo - or return Node

    def add_element(self, new_word):
        pass

    def find_elements(self, search_string):
        return 0

if __name__ == "__main__":
    R = Node()
    n = int(input().strip())
    for a0 in range(n):
        op, contact = input().strip().split(' ')
        if op == "add":
            R.add_element(contact)
        elif op == "find":
            results = R.find_elements(contact)
            print(results)
