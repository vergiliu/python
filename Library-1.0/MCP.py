
from __future__ import print_function
import cmd

# das magische cli parsierung

class magiccliparser(cmd.Cmd):
    def do_EOF(self, line):
        self.cleanupstuff()
        return True

    def do_stuff(self, line):
        """ about stuff """
        print("something")
    def do_help(self, line):
        """ help """
        print ("help help help")

    def do_exit(self, line):
        """quit"""
        self.do_quit(line)

    def do_quit(self, line):
        """quit"""
        self.cleanupstuff()
        exit()

    def cleanupstuff(self):
        print("closing")

    def startit(self):
        self.prompt = "A "
        self.cmdloop()

if __name__ == "__main__":
    print("should not be called directly")

