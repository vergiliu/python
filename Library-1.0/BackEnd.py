from __future__ import print_function
import os
import sys
import time
import json
import zmq

class BackEnd:
    """BackEnd should handle all of the processing"""

    def __init__(self, port=49152, host="127.0.0.1"):
        self.port=port
        self.host=host
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        connection_string = "tcp://"+ host +":"+ str(port) 
        socket.bind(connection_string)
        self.S = socket

    def run(self):
        print("port = %d" % self.port)
        print("host = %s" % self.host)
        jd = json.JSONDecoder()
        jc = json.JSONEncoder()
        #ACK = {'cmd': 'ACK', 'data': None}
        while True:
            msg = self.S.recv()
            self.processMessage(jd, msg)
            self.S.send("ACK")
        print(" for cli and api/app communication")

    def processMessage(self, aJsonDecoder, aMessage):
        myData = aJsonDecoder.decode(aMessage)
        print("command = %s data = %s" % (myData['cmd'], myData['data']))
        if myData['cmd'] == "exit":
            self.S.send("BYE")
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
        pass

    def cleanup(self):
        print("cleanup ")
        self.exit()
        # TODO

    def exit(self):
        print("exit")

def jeison():
    # http://cpiekarski.com/2011/05/09/super-easy-python-json-client-server/
    # http://stackoverflow.com/questions/1712249/python-json-rpc-server-with-ability-to-stream
    jc = json.JSONEncoder()
    jd = json.JSONDecoder()

    mydict_send = {'command': 'test', 'data': None}

    mydata = jc.encode(mydict)
    # send mydata
    # receive mydata_recv
    mydict_recv = jd.decode(mydata_recv)

if __name__ == "__main__":
    print("starting")
    B = BackEnd()
    B.run()
    print("done")
