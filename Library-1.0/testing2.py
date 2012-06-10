import threading
import thread
import time
import sys
import os

class TTest(threading.Thread):
    def __init__(self, event, name):
        threading.Thread.__init__(self)
        print "init"
        self.event = event
        self.name = name

    def setEvent(self):
        self.event.set()
        print "set " + self.name

    def clearEvent(self):
        self.event.clear()
        print "clear " +self.name
        
    def waitEvent(self):
        self.event.wait()
        print "wait " +self.name

    def run(self):
        print "running " +self.name
        self.waitEvent()

class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.theRootPaths = []
        self.theFiles = []

    def run(self):
        self.findFilesInPath()

    def findFilesInPath(self):
        for myPath in self.theRootPaths:
            for dirpath, dirnames, filenames in os.walk(myPath):
                for filename in filenames:
                    self.theFiles.append(dirpath + "/" + filename)

    def addPath(self, aPath):
        if os.access(aPath, os.R_OK):
            self.theRootPaths.append(aPath)
        else:
            print "path "+ aPath +"can't be added"

class AllFiles():
    def __init__(self):
        self.theFiles = []

    def addPath(self, aLocalRootFolder):
        if os.access(os.path.expanduser(aLocalRootFolder), os.R_OK):
            for dirpath, dirnames, filenames in os.walk(os.path.expanduser(aLocalRootFolder)):
                for filename in filenames:
                    self.theFiles.append(dirpath + "/" + filename)
                #for dire in dirnames:
                #    print ">> " + dire
                # useless    
        else:
            print "ERR monkey"
            # TODO raise

    def findAllFiles(self, anExtension):
        myTemp = []
        for myFile in self.theFiles:
            if myFile.endswith(anExtension):
                myTemp.append(myFile)
        return myTemp

    def howManyFiles(self):
        return len(self.theFiles)

if __name__ == "__main__":
    ana = A()

    # TODO read from file, right at startup
    ana.addPath("~")
    ana.addPath("/home/123")
    ana.addPath("~/Desktop")
    ana.start()
    print len(ana.theFiles), "files, size ana = ", int(sys.getsizeof(ana.theFiles)/1024) , "KB"
    print("almost done...")


    e = threading.Event()
    x = TTest(e, "X")
    y = TTest(e, "Y")
    x.start()
    y.start()
    time.sleep(1)
    y.setEvent()
    x.setEvent()
    print x.is_alive()
    print "==="
    myFiles = AllFiles()
    myFiles.addPath("~")
    myFiles.addPath("/home/123")
    myFiles.addPath("~/Desktop")
    #print myFiles.findAllFiles("txt")
    print "total files ", myFiles.howManyFiles()
    print "size = ", int(sys.getsizeof(myFiles.theFiles)/1024) , "KB"
    print len(ana.theFiles), "files, size ana = ", int(sys.getsizeof(ana.theFiles)/1024) , "KB"

    #http://docs.python.org/library/queue.html?highlight=queue#Queue 