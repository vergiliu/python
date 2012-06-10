import multiprocessing
from MCP import magiccliparser

m = magiccliparser()

print ("CPU count = %d" % multiprocessing.cpu_count())

m.startCLI()
