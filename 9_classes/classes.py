'''
3h02m
Simple types: Numbers, Strings, Booleans
Complex: Lists, Dictionaries

To create out own type. We use classes. This is a blueprint of an object
'''

class Point: #For class, capitalise the first letter of every word
    def __init__(self, x, y): #constructor. Initalise the method
        self.x = x
        self.y = y
    def move(self): #This creates specific methods
        print('move')
    
    def draw(self):
        print('draw')

##This calls the __init__ method
point = Point(10, 20)
print(point.x)

##This uses the draw method defined above
#point1.draw()

##This creates an attribute on point
#point1 = Point()
#point1.x = 10 #This sets an attribute
#point1.y = 20
#print(point1.x)

##New object is a different instance of points class
#point2 = Point()
#point2.x = 1
#print(point2.x)