
class UserInterface:
    
    def __init__(self):
        self.filePath = None
                   
    def fileMode(self):
        mode = raw_input("File mode ? [Y/N]: ")
        if mode in ["y", "Y"]:
            defaultMode = raw_input("Default file mode ? [Y/N]: ")
            if defaultMode in ["y", "Y"]:
                self.filePath = "data.csv"
            else:
                self.filePath = raw_input("Enter file path: ")
            return True
        else:
            return False
    
    def getInput(self):
        table = []
        length = int(raw_input("table length: "))
        heigth = int(raw_input("table heigth: "))
        
        print "Insert row data divided by commas in ex: 1,2,3,5 \n"
        for i in range(heigth):
            data = raw_input("%d-row data: " %(i+1))
            row = data.split(",")
            print data
            if len(row) <= length:
                table.append(row)
            else:
                raise IOError("too many values in row")
        return table, length, heigth