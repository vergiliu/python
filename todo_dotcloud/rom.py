from todos import AAA
import pprint

class Listele():
    def __init__(self):
        self.datele = []

    def add(self, element):
        self.datele.append(element)

    def get(self, element):
        return self.datele[element]

if __name__=="__main__":
    x = Listele()
    unu = raw_input("1:")
    doi = raw_input("2:")

    olista = AAA(unu)
    incauna = AAA(doi)

    olista.add_RI()
    olista.add_RI()
    incauna.add_RI()
    x.add(olista)
    x.add(incauna)

    print "---"
    pprint.pprint(x.get(0).printElements())
    pprint.pprint(x.get(1).printElements())
    print "---"
    pprint.pprint(x)

