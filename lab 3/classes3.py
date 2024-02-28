class Shape:
    def __init__(self, area = 0):
        self.area = area

class Rectangle(Shape):
    def __init__(self, width = 0, length = 0):
        self.width = width
        self.length = length

    def getParameters(self):
        self.width = int(input("Vvedite wirinu: "))
        self.length = int(input("Vvedite dlinu: "))

    def printArea(self):
        self.area = self.width * self.length
        return self.area

a = Rectangle()
a.getParameters()
print("Area of this Rectangle is equals:", a.printArea())