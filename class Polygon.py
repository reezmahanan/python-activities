class Polygon: 
    def _init_(self, length, breadth):    
        self.__length = length
        self.__breadth = breadth

    def set_length(self, length):   #Setter Creation
        self.__length = length
    def set_breadth(self, breadth):
        self.__breadth = breadth

    def get_length(self):   #Getter Creation
        return self.__length
    def seg_breadth(self):
        return self.__breadth

class Rectangle(Polygon):   #Creating sub classes of Polygon class
    def area(self): #Area calculation function
        area = self.Polygonlength * self._Polygon_breadth
        return area

class Square(Polygon):
    def _init_(self, length): #Subclass specific variable initialision to only pass one variable to suqare
        self.__length = length

    def area(self):
        area = self.__length ** 2
        return area

if _name_ == '_main_':  
    rectangleLength = float(input("Enter the length of rectangle: "))   
    rectangleBreadth = float(input("Enter the breadth of rectangle: "))
    squareLength = float(input("Enter the length of square: "))
    
    rectangleObject = Rectangle(rectangleLength, rectangleBreadth)  
    squareObject = Square(squareLength)
    
    print(f"The area of a rectangle is {rectangleObject.area()}")   
    print(f"The area of a square is {squareObject.area()}")