"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.

Hint
Use __init__ method to construct some parameters

"""
class Exercise:
    def __init__(self):
        pass
    
    def getString(self):
        self.string = input("Enter a string: ")
        
    def printString(self):
        return print(self.string.upper())
        
test = Exercise()
test.getString()
test.printString()