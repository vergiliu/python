class People:
    def __init__(self, name):
        self.name = name
        self.bankAccount = {}

    def addBankAccount(self, anAccount):
        self.bankAccount[anAccount.getName()] = anAccount
        return self.bankAccount[anAccount.getName()].getName()

    def drawAmount(self, anAmount, anAccount):
        if self.bankAccount.has_key(anAccount):
            if self.bankAccount[anAccount].getSum() <= 0:
                raise ValueError('Insufficient funds to withdraw money')
            else:
                return self.bankAccount[anAccount].draw(anAmount)
        else:
            raise ValueError("No bank account used")

    def addAmount(self, anAmount, anAccount):
        if self.bankAccount.has_key(anAccount):
            return self.bankAccount[anAccount].add(anAmount)

    def getAccounts(self):
        for (bank, bankAccnt) in self.bankAccount.iteritems():
            print "bank = %s sum = %d" %(bank, bankAccnt.amount)

    def wireMoneyTo(self, person, anAmount):
        if len(self.bankAccount.keys()) >= 1:
            myAccount = self.bankAccount[self.bankAccount.keys()[0]]
        else:
            myAccount = None
        if len(person.bankAccount.keys()) >= 1:
            toAccount = person.bankAccount[person.bankAccount.keys()[0]]
        else:
            toAccount = None
        t = Transaction(myAccount, toAccount)
        return t.transfer(anAmount)

class BankAccount:
    def __init__(self, aName, initialAmount):
        self.bankName = aName
        self.amount = initialAmount
    def add(self, amount):
        self.amount += abs(amount)
        return self.amount
    def draw(self, amount):
        self.amount -= abs(amount)
        return self.amount
    def getName(self):
        return self.bankName
    def getSum(self):
        return self.amount

class Transaction:
    def    __init__(self, acc1, acc2):
        if not acc1 or not acc2 :
            raise ValueError("Invalid transaction")
        self.account_from = acc1
        self.account_to = acc2

    def transfer(self, anAmount):
        self.account_from.draw(anAmount)
        self.account_to.add(anAmount)
        return anAmount
