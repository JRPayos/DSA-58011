class Rectangle:
   def __init__(self,length,width):
     self.length = length
     self.width = width

   def Perimeter(self):
       print(2 * (self.length + self.width))


rect = Rectangle(7,3)
print( "Perimeter of the Rectangle:")
rect.Perimeter()

