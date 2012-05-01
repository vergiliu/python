import math 
import sys
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def isPrime(N):
    for n in xrange(2,int(math.sqrt(N))+1):
        if 0 == N % n:
            return False
    return True

if __name__ == "__main__":
    primes = []
    for i in xrange (1, int(sys.argv[1])):
        if isPrime(i):
            primes.append(i)
            if 10002 == len(primes):
                print primes[-1:]
    rest = 600851475143
    primes.reverse()
    for value in primes:
        if 0 == rest % value:
            rest = rest / value
            print value
            break
