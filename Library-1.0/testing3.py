from MCP import magiccliparser
import yaml
import pprint

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