import os
import sys
import time
import json
import zmq

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

    def run(self):
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
        myConfig.getConfigurationForSection('server')

    def cleanup(self):
        print("cleaning up")
        print("closing ZMQ socket")
        self.theSocket.close()
        print("destroying ZMQ context")
        self.theContext.destroy()
        exit()

if __name__ == "__main__":
    print("BackEnd starting")
    B = BackEnd()
    B.run()
    print("BackEnd stopped")
