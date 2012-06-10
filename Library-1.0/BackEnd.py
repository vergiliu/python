import os
import sys
import time
import json
import zmq
import threading

import ConfigReader
from process_text import ProcessText

# TODO handle Ctrl+C to stop cleanly
class BackEnd:
    """BackEnd should handle all of the processing"""

    def __init__(self, port=49152, host="127.0.0.1"):
        self.port=port
        self.host=host
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        connection_string = "tcp://"+ host +":"+ str(port) 
        socket.bind(connection_string)
        self.theContext = context
        self.theSocket = socket
        self.theScanner = None

    def running(self):
        self.startup()
        jd = json.JSONDecoder()
        jc = json.JSONEncoder()
        while True:
            msg = self.theSocket.recv()
            self.processMessage(jd, msg)
            self.theSocket.send("ACK")

    def processMessage(self, aJsonDecoder, aMessage):
        myData = aJsonDecoder.decode(aMessage)
        print("command = %s ( data = %s )" % (myData['cmd'], myData['data']))
        if   myData['cmd'] == "exit" or myData['cmd'] == "quit":
            self.theSocket.send("BYE")
            self.cleanup()
        elif myData['cmd'] == "process_text":
            aProcessor = ProcessText()
            aProcessor.start()
            print("starting process_text module")

    def startup(self):
        """
        start t1
        init communication with a/a/c
        wait for debug/fix mode / cripple - for 5sec (configurable time)

        start t2
        indexing
        save in memory
        """
        print("Running on host = %s : %d" % (self.host, self.port))
        myConfig = ConfigReader.ConfigReader()
        myConfig.loadConfigurationFile('config.yaml')
        myServerConfig = myConfig.getConfigurationForSection('server')
        myFolders = myServerConfig.get('parseFolders')

        print("BackEnd starting")
        myEvent = threading.Event()
        self.theScanner = ScanPaths(myEvent)

        if myFolders:
            self.theScanner.addPaths(myFolders)
        else:
            print("Error: could not find any folders configured YAML:[server -> parseFolders]")
            exit(1)
            # TODO raise/throw
        self.theScanner.start()
        myEvent.wait()
        print("Startup finished")

    def cleanup(self):
        print("cleaning up")
        print("closing ZMQ socket")
        self.theSocket.close()
        print("destroying ZMQ context")
        self.theContext.destroy()
        exit()

class ScanPaths(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.theRootPaths = []
        self.theFiles = []
        self.theEvent = event

    def run(self):
        self.findFilesInPath()
        self.theEvent.set()

    def findFilesInPath(self):
        self.theEvent.clear()
        for myPath in self.theRootPaths:
            for dirpath, dirnames, filenames in os.walk(myPath):
                for filename in filenames:
                    self.theFiles.append(dirpath + "/" + filename)
                #for dirs in dirnames:
                #    print ">> " + dirs ### useless    

    def addPath(self, aPath):
        myExpandedPath = os.path.expanduser(aPath)
        if os.access(myExpandedPath, os.R_OK):
            self.theRootPaths.append(myExpandedPath)
        else:
            print ("The path " + myExpandedPath + " can't be added")

    def addPaths(self, aPaths):
        for myPath in aPaths:
            self.addPath(myPath)

    def findAllFiles(self, anExtension):
        myTemp = []
        for myFile in self.theFiles:
            if myFile.endswith(anExtension):
                myTemp.append(myFile)
        return myTemp

    def howManyFiles(self):
        return len(self.theFiles)

if __name__ == "__main__":
    myServer = BackEnd()
    myServer.running()
    print("BackEnd stopped")
