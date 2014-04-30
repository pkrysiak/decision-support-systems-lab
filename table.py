
class Value:
    
    def __init__(self, value):
        self.value = float(value)
        self.sum = float(value)
        self.pointer = None
        
    def __repr__(self):
        return ' - '.join([str(x) for x in [self.value,self.sum]])

        
class Table:
    '''
        Table Class which contains dynamic programming algorithm which allows to 
        count shortest path.
        
        Task:
        We put pawn at some field in the first column of the board. From the point 
        which have coordinates x,y pawn can move to coordinates x+1,y+1, x+1,y, x+1,y-1
        (where x is length and y is heigth coordinate). We have to calculate length of the
        shortest path that pawn can take to travel across the board.
    '''
    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.table = [[] for x in range(self.height)]        
        self.addedValues = 0
    
    def addMultipleValues(self, inputTable):
        for row in inputTable:
            for col in row:
                self.__addValue(col)
        
    def processTable(self):
        assert self.addedValues == self.length * self.height, "not all values were added to this table"
        self.__addSpecialRows()
        
        for colNumber in range(1,self.length):
            for rowNumber in range(1,self.height+1):
                current = self.table[rowNumber][colNumber]
                previousUpper = self.table[rowNumber - 1][colNumber - 1]
                previous = self.table[rowNumber][colNumber - 1]
                previousLower = self.table[rowNumber + 1][colNumber - 1]
                previousMin = self.__valuesMin(previousUpper, previous, previousLower)
                current.sum = current.value + previousMin.sum
                current.pointer = previousMin
        return self.__lastColumnMin().sum
    
    def retreiveMinSequence(self):
        sequence = []
        field = self.__lastColumnMin()
        while True:
            sequence.append(field.value)
            field = field.pointer
            if field.pointer == None:
                sequence.append(field.value)
                break            
        return sequence
    
    
    def showTable(self):
        for row in self.table[1:-1]:
            print row
    
    def __addValue(self, value):
        newValue = Value(value)
        rowNumber = self.addedValues / self.length
        if len(self.table[rowNumber]) < self.length:
            self.table[rowNumber].append(newValue)
            self.addedValues += 1
    
    def __addSpecialRows(self):
        specialRow = [Value(float("inf")) for x in range(self.length)]
        self.table.insert(0, specialRow)
        self.table.append(specialRow)  
    
    def __valuesMin(self, val1, val2, val3):
        return min(val1, val2, val3, key= lambda value: value.sum)
    
    def __lastColumnValues(self):
        return [x[-1] for x in self.table]        
             
    def __lastColumnMin(self):
        return min(self.__lastColumnValues(), key=lambda v: v.sum)      
        