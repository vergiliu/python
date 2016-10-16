class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
    # todo - keep state
    # todo - or return Node

    def add_element(self, new_word):
        if new_word != '':
            if new_word[0] in self.children:
                self.children[new_word[0]].add_element(new_word[1:])
            else:
                self.children[new_word[0]] = Node()
                self.children[new_word[0]].add_element(new_word[1:])
        else:
            self.isWord = True

    def find_elements(self, search_string):
        found = 0
        for k in self.children:
            if k == search_string[0]:
                if len(search_string) == 1:
                    if self.children[k].isWord:
                        found += 1
                    else:
                        found += self.countAllWords()
                else:
                    found += self.children[k].find_elements(search_string[1:])
        return found

    def debug_display(self):
        for k in self.children:
            print("{}".format( k), end="")
            if self.children[k].isWord: print()
            self.children[k].debug_display()

    def countAllWords(self):
        found =0
        for k in self.children:
            if self.children[k].isWord:
                found += 1
            self.children[k].countAllWords()
        return found


if __name__ == "__main__":
    import sys

    R = Node()
    if len(sys.argv) == 2:
        n = int(input().strip())
        for a0 in range(n):
            op, contact = input().strip().split(' ')
        if op == "add":
            R.add_element(contact)
            # R.debug_display()
        elif op == "find":
            results = R.find_elements(contact)
            print(results)

    else:
        R.add_element("habi")
        # R.debug_display()
        R.add_element("haci")
        # R.debug_display()
        R.add_element("B")
        R.debug_display()
        print(R.find_elements("B"))

            # R.debug_display(0)
