class Twomethods(object):
    def __init__(self):
        pass
    def getString(self,input_string):
        return input_string
    def printString(self, prtstr):
        return print(prtstr.uppercase())
a = str(input())
b = Twomethods()
result = Twomethods.getString()
result = Twomethods.printString()
