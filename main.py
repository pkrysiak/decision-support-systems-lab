'''
  Pawel Krysiak
  216568    
  Decision support systems
  Dynamic Programming
'''
from parser import *
from table import *
from ui import *

class Main:
    def __init__(self):  
        userInterface = UserInterface()
        if userInterface.fileMode():                 
            fileContent = CSVParser(userInterface.filePath)
            table = Table(fileContent.length(), fileContent.heigth())
            table.addMultipleValues(fileContent.parseFile())            
        else:
            userInput, length, heigth = userInterface.getInput()
            table = Table(length, heigth)
            table.addMultipleValues(userInput)
        print "Min distance: ", table.processTable()
        print "Min path:", table.retreiveMinSequence()
            
if __name__ == "__main__":
    Main()
    
    
        