import yaml
import pprint
import os

# author: vergiliu

class ConfigReader:
    """ ConfigReader class will handle the configuration file
    uses external PyYAML dependency to parse, read, and save the configuration file
    uses prettyprint to dump the configuration if needed"""
    def __init__(self):
        self.theConfigurationData = None
        self.theConfigurationFile = None

    # TODO throw exception instead of exit
    def loadConfigurationFile(self, aFilename):
        """Load the configration from a YAML file"""
        if not os.access(aFilename, os.O_RDWR):
            print("ERROR: could not open configuration file - ", aFilename)
            exit(1)
        else:
            self.theConfigurationFile = aFilename
            myConfigurationFile = open(aFilename)
            self.theConfigurationData = yaml.load(myConfigurationFile)
            myConfigurationFile.close()           

    def saveConfigurationFile(self):
        """Save the configuration changes back to the file"""
        pass

    # TODO throw, or return something else
    def getConfigurationForSection(self, aKey):
        if self.theConfigurationData.get(aKey):
            return self.theConfigurationData[aKey]
        else:
            return None

    def printConfiguration(self):
        print("configuration data:")
        pprint.pprint(self.theConfigurationData)

if __name__ == "__main__":
    print("must not be called directly")
