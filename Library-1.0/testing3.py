from MCP import magiccliparser
import yaml
import pprint
import queue

import ConfigReader

if __name__ == "__main__":
    cli = magiccliparser()

    f = open('config.yaml')
    dataMap = yaml.load(f)
    f.close()

    pprint.pprint(dataMap)
    print(dataMap['server']['parseFolders'])

    x = ConfigReader.ConfigReader()
    x.loadConfigurationFile('config.yaml')
    x.printConfiguration()
    print(x.getConfigurationForSection('server')['parseFolders'])

    ### Queues

    myQ = queue.Queue()
    print(myQ.qsize())
    x = {'ana': 'are mere', 'costel': ['nu', 'are']}
    y = {'oana': 'are mere', 'gigel': ['nu', 'are']}
    myQ.put(x)
    myQ.put_nowait(y)
    print(myQ.qsize())
    print(myQ.get().keys())
    print(myQ.get().keys())
    print(myQ.qsize())