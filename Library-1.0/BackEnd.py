from __future__ import print_function
import os
import sys
import time
import json
import zmq

# http://cpiekarski.com/2011/05/09/super-easy-python-json-client-server/
# http://stackoverflow.com/questions/1712249/python-json-rpc-server-with-ability-to-stream

class BackEnd:
    """BackEnd should handle all of the processing"""

    def __init__(self, port=49152, host="127.0.0.1"):
        self.port=port
        self.host=host
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        connection_string = "tcp://"+ host +":"+ str(port) 
        socket.bind(connection_string)
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
        if myData['cmd'] == "exit":
            self.theSocket.send("BYE")
            self.cleanup()

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

    def cleanup(self):
        print("cleanup ")
        exit()
        # TODO

if __name__ == "__main__":
    print("BackEnd starting")
    B = BackEnd()
    B.run()
    print("BackEnd stopped")
