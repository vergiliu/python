from __future__ import print_function

import urllib2, simplejson
import pprint as pretty
import getopt as getoptions
import sys

MAIN_URL = "http://api.ihackernews.com/"

# proxy: http://www.wkoorts.com/wkblog/2008/10/27/python-proxy-client-connections-requiring-authentication-using-urllib2-proxyhandler/
# urllib : http://www.voidspace.org.uk/python/articles/urllib2.shtml
# urllib: http://docs.python.org/release/2.4.4/lib/urllib2-examples.html
# http://docs.python.org/library/urllib2.html#urllib2.ProxyHandler
# http://www.saltycrane.com/blog/2008/08/using-python-digg-api-and-simplejson/
# http://developer.yahoo.com/python/python-json.html

class configurationData():
    PROXY = {}
    POINTS_LIMIT = 0
    def setPointsLimit(self, PL):
        self.POINTS_LIMIT = int(PL)
    def getPointsLimit(self):
        return self.POINTS_LIMIT
    def setProxy(self, proxyHost):
        self.PROXY[proxyHost.split(':')[0]] = proxyHost
    def getProxy(self):
        return self.PROXY
    def printConfig(self):
        print("PROXY is %s" % self.PROXY)
        print("POINTS_LIMIT is %d" % self.POINTS_LIMIT)
    def setAddress(self, type):
        self.accessPage = type
    def getAddress(self):
        return self.accessPage

def makeRequest(aConfig):
    proxy_support = urllib2.ProxyHandler(aConfig.getProxy())
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    results = simplejson.load(urllib2.urlopen(MAIN_URL + aConfig.getAddress()))
    try:
        myFile = open("last_", "rt")
        lastFileTitle = myFile.readline()
        myFile.close()
    except:
        lastFileTitle = None    
    myNextId = results['nextId']
    myHNVersion = results['version']
    lastTitle = results['items'][0]['title']
    print ("current version is %s / next page on %s " % (myHNVersion, MAIN_URL+str(myNextId)))
    canPrint = True
    PL = aConfig.getPointsLimit()
    for myArticle in results['items']:
        if canPrint and int(myArticle['points']) >= PL:
            print ("%4d %s (%4d)" % (myArticle['points'], myArticle['title'], myArticle['commentCount'])),
            print ("     %s" % myArticle['url'])
        if ( lastFileTitle and lastFileTitle == myArticle['title'] ):
            canPrint = False
    myFile = open("last_", "wt")
    myFile.write(lastTitle)
    myFile.close()
    # pretty.pprint (results)

def showUsage():
    print ("%s [-h|--help] [-x|--proxy http|ftp://proxy_server] [--points LIMIT] <-n|--new>|<-p|--page>" % sys.argv[0])
    sys.exit()

def parseOptions(arguments, configurationData):
    # print ("arguments = %s", arguments)
    try:
        options, others = getoptions.getopt(arguments, 'nphx:', ['help', 'proxy=', 'points='])
    except getoptions.GetoptError, err:
        print (str(err))
        sys.exit()
    for mySelection, myValue in options:
        if mySelection in ('-x', '--proxy'):
            configurationData.setProxy(myValue)
            print ("Using proxy %s" % configurationData.getProxy())
        elif mySelection in ('-h', '--help'):
            showUsage()
        elif mySelection in ('-n'):
            configurationData.setAddress('new')
        elif mySelection in ('-p'):
            configurationData.setAddress('page')
        elif mySelection in ('--points'):
            configurationData.setPointsLimit(myValue)

if __name__ == '__main__':
    ## add getopt parsing - done
    if len(sys.argv) == 1:
        showUsage()
    myConfig = configurationData()
    parseOptions(sys.argv[1:], myConfig)
    ## add proxy handling if given - done
    # myConfig.printConfig()
    # sys.exit()
    makeRequest(myConfig)
    ## add handling of cookies or files
    ## add over # of points if given
