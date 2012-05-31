from __future__ import print_function
import os
import sys
import time
import json

class Bend:
    def __init__(self, port=59152, host="localhost"):
        self.port=port
        self.host=host

    def dostuff(self):
        print("port = %d" % self.port)
        print("host = %s" % self.host)
        print(" import json or simplejson")
        #...
        print(" for cli and api/app communication")

    def startup(self):
        """
        start t1
        init communication with a/a/c
        wait for debug/fix mode / cripple - for 5sec (configurable time)

        start t2
        indexing
        save in memory
        """

    def exit(self):
        print("exit")

def jeison():
    # http://cpiekarski.com/2011/05/09/super-easy-python-json-client-server/
    # http://stackoverflow.com/questions/1712249/python-json-rpc-server-with-ability-to-stream
    jc = json.JSONEncoder()
    jd = json.JSONDecoder()

    mydict_send = {'command': 'test', 'data': }

    mydata = jc.encode(mydict)
    # send mydata
    # receive mydata_recv
    mydict_recv = jd.decode(mydata_recv)

if __name__ == "__main__":
    print("starting")
    B = Bend()
    B.dostuff()
    print("done")


