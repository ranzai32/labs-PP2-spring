class Shape:
    def __init__(self, area = 0): #init - initialization - создаешь переменную
        self.area = area

class Square(Shape):
    def __init__(self, length = 0):
        self.length = length

    def getLength(self):
        self.length = int(input("Type length:"))

    def calculateArea(self):
        self.area = self.length * self.length
        return self.area
a = Square()
a.getLength()
print("Area is equal", a.calculateArea())
