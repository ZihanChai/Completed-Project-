from math import sin, radians

class Parallelogram():
    '''A class representing a parallelogram with a base, side and theta'''

    def __init__(self, base, side, theta):
        '''(Parallelogram, int, int, int) -> NoneType
        Create a new parallelogram with base, side and theta.
        REQ: base >= 0
        REQ: side >= 0
        REQ: theta >= 0, <= 360
        '''
        self.base = base
        self.side = side
        self.theta = theta

    def area(self):
        '''(Parallelogram) -> float
        Return the area of the Parallelogram.
        '''
        return self.base * self.side * sin(radians(self.theta))

    def bst(self):
        '''(Parallelogram) -> list of float
        Return the base, side and theta of the Parallelogram in order in a list
        '''
        # Create an empty list
        new_list = []
        # Add the base, side and theta of the square in order to the list
        new_list.append(float(self.base))
        new_list.append(float(self.side))
        new_list.append(float(self.theta))
        return new_list

    def __str__(self):
        '''(Parallelogram) -> str
        Return the string state the shape and the area of the graph
        '''
        return "I am a Parallelogram with area " + str(int(self.area()))

class Rectangle(Parallelogram):
    '''A class representing a Rectangle with a base, side'''

    def __init__(self, base, side):
        '''(Rectangle, int, int) -> NoneType
        Create a new rectangle with base and side.
        REQ: base >= 0
        REQ: side >= 0
        '''
        # Call the inheritance function
        Parallelogram.__init__(self, base, side, 90)

    def area(self):
        '''(Rectangle) -> float
        Return the area of the rectangle.
        '''
        return self.base * self.side

    def bst(self):
        '''(Rectangle) -> list of float
        Return the base, side and theta of the Rectangle in order in a list
        '''
        # Create an empty list
        new_list = []
        # Add the base, side and theta of the square in order to the list
        new_list.append(float(self.base))
        new_list.append(float(self.side))
        new_list.append(90.0)
        return new_list

    def __str__(self):
        '''(Rectangle) -> str
        Return the string state the shape and the area of the graph
        '''
        return "I am a Rectangle with area " + str(int(self.area()))

class Rhombus(Parallelogram):
    '''A class representing a rhombus with a base and theta'''
    
    def __init__(self, base, theta):
        '''(rhombus, int, int) -> NoneType
        Create a new rhombus with base and theta.
        REQ: base >= 0
        REQ: theta >= 0, <= 360
        '''
        # Call the inheritance function
        Parallelogram.__init__(self, base, base, theta)

    def area(self):
        '''(rhombus) -> float
        Return the area of the rhombus.
        '''
        return self.base * self.base * sin(radians(self.theta))

    def bst(self):
        '''(rhombus) -> list of float
        Return the base, side and theta of the rhombus in order in a list
        '''
        # Create an empty list
        new_list = []
        # Add the base, side and theta of the square in order to the list
        new_list.append(float(self.base))
        new_list.append(float(self.base))
        new_list.append(float(self.theta))
        return new_list

    def __str__(self):
        '''(rhombus) -> str
        Return the string state the shape and the area of the graph
        '''
        return "I am a Rhombus with area " + str(int(self.area()))

class Square(Parallelogram):
    '''A class representing a square with a base and theta'''

    def __init__(self, base):
        '''(square, int) -> NoneType
        Create a new square with base.
        REQ: base >= 0
        '''
        # Call the inheritance function
        Parallelogram.__init__(self, base, base, 90)

    def area(self):
        '''(square) -> float
        Return the area of the square.
        '''
        return self.base * self.base

    def bst(self):
        '''(square) -> list of float
        Return the base, side and theta of the square in order in a list
        '''
        # Create an empty list
        new_list = []
        # Add the base, side and theta of the square in order to the list
        new_list.append(float(self.base))
        new_list.append(float(self.base))
        new_list.append(90.0)
        return new_list

    def __str__(self):
        '''(square) -> str
        Return the string state the shape and the area of the graph
        '''
        return "I am a Square with area " + str(int(self.area()))
