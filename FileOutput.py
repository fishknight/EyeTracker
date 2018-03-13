import json
import Constants

class FileOutput():
    def __init__(self):
        file = open(Constants.FILENAME, 'r+')

    def writeArrayToFile(self, array):
        self.output = json.dumps(array)
    