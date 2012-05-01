# author: Vergiliu, 20 Jan 2011
# fb puzzle # 2

import sys

def updateDict(accuserNames, currentAccuser, inputFile, suggestions):
    for index in xrange(0, suggestions):
        name = inputFile.readline().strip()
        accuserNames[currentAccuser]['liars'].append(name)
        if not accuserNames.has_key(name):
            accuserNames[name] = {'profile': 1, 'liars':[], 'lied':False}
        else:
            accuserNames[name]['profile'] += 1

def liarLiarPantsOnFire(noAcc, inputFile):
    for accuser in xrange(1, noAcc+1):
        (name, suggestions) = inputFile.readline().strip().split()
        if not accuserNames.has_key(name):
            accuserNames[name] = {'profile': .5, 'liars':[], 'lied':False}
        else:
            accuserNames[name]['profile'] += .5
        updateDict(accuserNames, name, inputFile, int(suggestions))
    # here we can optimize the max function, but let's not do that yet
    # or we could have done that when computing ;)
    maxvalue=[0, '']
    for accuser in accuserNames.keys():
        if accuserNames[accuser]['profile'] > maxvalue[0]:
            maxvalue[0] = accuserNames[accuser]['profile']
            maxvalue[1] = accuser
    return maxvalue

if __name__ == "__main__":
    try:    
        myFile = open(sys.argv[1])
    except:
        sys.exit(-1)

    accuserNames={}
    oneLiar=[]
    numberAccusers = int(myFile.readline().strip())
    oneLiar = liarLiarPantsOnFire(numberAccusers, myFile)
#    print accuserNames
#    print oneLiar
    (sayingTruth, lying) = (0, 0)

    for accuser in accuserNames.keys():
        # we can mark future liars in here so it will be faster
        # if we iterate over big sets
        if oneLiar[1] in accuserNames[accuser]['liars']:
            lying += 1
        else:
            sayingTruth += 1

    print "%d %d" % (lying, sayingTruth)
    
    

