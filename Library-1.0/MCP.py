from __future__ import print_function

import zmq
import json
import cmd

# das magische cli parsierung

class magiccliparser(cmd.Cmd):

    def do_EOF(self, line):
        self.cleanupstuff()
        return True

    def do_stuff(self, line):
        """ about stuff """
        print("something")

    def do_stop_server(self, line):
        data = self.theJsonEncoder.encode({'cmd': 'exit', 'data': None})
        self.theSocket.send(data)
        if self.theSocket.recv() == "BYE":
            print("server is stopped")

    def do_send(self, line):
        """ send <data> to server"""
        print("data to send = [%s]" % line)
        data = self.theJsonEncoder.encode({'cmd': 'todo', 'data': line})
        self.theSocket.send(data)
        recv = self.theSocket.recv()
        print("got %s" % recv)

#    def do_help(self, line):
#        """ override help function """
#        print ("help help help")

    def do_exit(self, line):
        """quit CLI"""
        self.do_quit(line)

    def do_quit(self, line):
        """quit CLI"""
        self.cleanupstuff()
        exit()

    def cleanupstuff(self):
        print("closing")

    def startit(self):
        self.prompt = "> "
        self.theJsonEncoder = json.JSONEncoder()
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:49152")
        self.theSocket = socket
        self.cmdloop()

if __name__ == "__main__":
    print("should not be called directly")

