from __future__ import print_function

import threading
import thread
import time
#import parseargs

# author: vergiliu
# purpose: threading tests, processing scanning for text files

# TODO add zmq processing of messages

class ProcessText(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		print("init")

	def run(self):
		print("ProcessText running...")
		while True:
			time.sleep(1)
			print(".", end=" ")


if __name__ == "__main__":
	print("cannot be called directly")