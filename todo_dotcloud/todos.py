class ToDo:
    def __init__(self, description):
        print "name = %s" % description
        self.description = description
        self.tasks = {}

    def getDescription(self):
        return self.description

    def add(self, taskDescription):
        self.tasks[self.getSize() + 1] = taskDescription

    def add_ReadInput(self):
        task = raw_input("ce? ")
        self.tasks[self.getSize() + 1] = task
    
    def printElements(self):
        print self.tasks
        for (k,v) in self.tasks.iteritems():
            print k,v
        print "XXX"
    
    def getSize(self):
        return len(self.tasks)

if __name__ == "__main__":
    a = AAA("test")
    
