# author: Vergiliu, 18 Jan 2011
# fb puzzle # 0

import sys

def hoppityhop(aNumber):
#    print "Using number: %d" % aNumber
    for counter in xrange(1, aNumber + 1):
        if counter % 3 == 0 and counter % 5 == 0:
            print "Hop"
        elif counter % 5 == 0:
            print "Hophop"
        elif counter % 3 == 0:
            print "Hoppity"

if __name__ == "__main__":
    try:    
        file = open(sys.argv[1])
    except:
        sys.exit(-1)
    hoppityhop(int(file.readline().strip()))
