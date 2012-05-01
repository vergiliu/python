def isPal(N):
    stringN = str(N)
    stringLen = len(stringN)
    first = stringN[:stringLen/2]
    if 0 == stringLen % 2:
        last = stringN[stringLen:stringLen/2-1:-1]
    else:
        last = stringN[stringLen:stringLen/2:-1]
    return first == last
 
if __name__ == "__main__":
    foundMaximum = 0
    for one in xrange(900,1000):
        for two in xrange(1000,900, -1):
            product = one*two
            if isPal(product) and foundMaximum < product:
                foundMaximum = product
    print foundMaximum