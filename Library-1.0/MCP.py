import zmq
import json
import cmd

class magiccliparser(cmd.Cmd):

    def do_stop_server(self, line):
        data = self.theJsonEncoder.encode({'cmd': 'exit', 'data': None})
        self.theSocket.send(data)
        #if self.theSocket.recv() == "BYE":
        #    print("server is stopped")

    def do_send_cmd(self, line):
        """  send a specific command (cmd field) to the server"""
        print("command to send = [%s]" % line)
        data = self.theJsonEncoder.encode({'cmd': line, 'data': None})
        self.theSocket.send(data)
        self.theSocket.recv()
        #print("got %s" % recv)

    def do_send_data(self, line):
        """  send some data (data field) to server"""
        if line:
            print("data to send = [%s]" % line)
            data = self.theJsonEncoder.encode({'cmd': 'new_data', 'data': line})
            self.theSocket.send(data)
            recv = self.theSocket.recv()
        else:
            print("no data to send")
        #print("got %s" % recv)

    def do_exit(self, line):
        """  quit the CLI when calling exit or quit"""
        self.do_quit(line)

    def do_quit(self, line):
        """  quit the CLI when calling exit or quit"""
        self.cleanupstuff()

    def do_EOF(self, line):
        """  quit the CLI when pressing Ctrl + C"""
        self.cleanupstuff()

    def cleanupstuff(self):
        print("\ncleaning up...\nclosing socket")
        self.theSocket.close()
        print("destroying ZMQ context")
        self.theContext.destroy()
        exit()

#    def do_help(self, line):
#        """ override help function """
#        print ("help help help")

    def startCLI(self):
        self.prompt = "# "
        self.theJsonEncoder = json.JSONEncoder()
        self.theContext = zmq.Context()
        socket = self.theContext.socket(zmq.REQ)
        socket.connect("tcp://localhost:49152")
        self.theSocket = socket
        self.cmdloop()

if __name__ == "__main__":
    print("must not be called directly")
