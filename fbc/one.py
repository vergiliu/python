# author: Vergiliu, 18 Jan 2011
# fb puzzle # 1

import sys

if __name__ == "__main__":
    try:    
        file = open(sys.argv[1])
    except:
        sys.exit(-1)
    print "Meep meep!"
