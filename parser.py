
import os,csv

class CSVParser:
    
    def __init__(self, filePath):
        self.filePath = filePath
    
    def parseFile(self):
        if not os.path.exists(self.filePath):
            raise IOError
        else:
            csvFile = open(self.filePath, 'rb')
            reader = csv.reader(csvFile, delimiter=' ')               
            return reader
    
    def length(self):
        csvFile = self.parseFile()
        for row in csvFile:
            return len(row)
    
    def heigth(self):
        colLen = 0
        csvFile = self.parseFile()
        for _ in csvFile:
            colLen += 1
        return colLen