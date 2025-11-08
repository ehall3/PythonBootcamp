# object_oriented.py
"""Python Essentials: Object Oriented Programming.
Ellison Hall 
Math Clinic 
November 8, 2025
"""

from math import sqrt
from sys import maxsize


class Backpack:
    """A Backpack object class. Has a name and a list of contents.

    Attributes:
        name (str): the name of the backpack's owner.
        contents (list): the contents of the backpack.
    """

    # Problem 1: Modify __init__() and put(), and write dump().
    def __init__(self, name, color, max_size = 5):
        """Set the name, color, max size ,and initializes an empty list of contents. If no max size is given, defaults to 5.

        Parameters:
            name (str): the name of the backpack's owner.
            color (str): the color of the backpack.
            max_size (int): the maximmum number of ideas allowed in the backpack.
        """
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []

    def put(self, item):
        """Add an item to the backpack's list of contents. If backpack is at capacity returns 'No Room!'."""

        if len(self.contents) >= self.max_size:
            print("No Room!")
        else:
            self.contents.append(item)

    def dump(self):
        """Resets contents of the backpack to empty"""
        self.contents = []

    def take(self, item):
        """Remove an item from the backpack's list of contents."""
        self.contents.remove(item)

    # Magic Methods -----------------------------------------------------------

    # Problem 3: Write __eq__() and __str__().
    def __eq__(self, other):
        """Determines if two backpacks have the same name, color, and number of contents"""
        return (self.name == other.name and 
                self.color == other.color and 
                len(self.contents) == len(other.contents))

    def __str__(self):
        """Returns the string of an object"""
        return (
            f"Owner:\t {self.name}\n"
            f"Color:\t {self.color}\n" 
            f"Size:\t {len(self.contents)}\n"
            f"Max Size:\t {self.max_size}\n"
            f"Contents:\t {self.contents}\n")


    def __add__(self, other):
        """Add the number of contents of each Backpack."""
        return len(self.contents) + len(other.contents)

    def __lt__(self, other):
        """Compare two backpacks. If 'self' has fewer contents
        than 'other', return True. Otherwise, return False.
        """
        return len(self.contents) < len(other.contents)


# An example of inheritance. You are not required to modify this class.
class Knapsack(Backpack):
    """A Knapsack object class. Inherits from the Backpack class.
    A knapsack is smaller than a backpack and can be tied closed.

    Attributes:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        contents (list): the contents of the backpack.
        closed (bool): whether or not the knapsack is tied shut.
    """
    def __init__(self, name, color):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. A knapsack only holds 3 item by default.

        Parameters:
            name (str): the name of the knapsack's owner.
            color (str): the color of the knapsack.
            max_size (int): the maximum number of items that can fit inside.
        """
        Backpack.__init__(self, name, color, max_size=3)
        self.closed = True

    def put(self, item):
        """If the knapsack is untied, use the Backpack.put() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.put(self, item)

    def take(self, item):
        """If the knapsack is untied, use the Backpack.take() method."""
        if self.closed:
            print("I'm closed!")
        else:
            Backpack.take(self, item)

    def weight(self):
        """Calculate the weight of the knapsack by counting the length of the
        string representations of each item in the contents list.
        """
        return sum(len(str(item)) for item in self.contents)


# Problem 2: Write a 'Jetpack' class that inherits from the 'Backpack' class.
class Jetpack(Backpack):
    """This is my awesome jetpack object class. Read it and weep. It can carry less
    than a knapsack but I can fly >:)
    Attributes:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        contents (list): the contents of the backpack.
        fuel (float): how much fuel I have to fly with.
    """

    def __init__(self, name, color, max_size = 2, fuel = 10):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. A jetpack only holds 2 items by default.

        Parameters:
            name (str): the name of the knapsack's owner.
            color (str): the color of the knapsack.
            max_size (int): the maximum number of items that can fit inside.
        """
        Backpack.__init__(self, name, color, max_size)
        self.fuel = fuel

    def fly(self, amount):
        """New Method of the Jetpack Class."""
        if amount > self.fuel:
            print ("Not enough fuel!")
        else:  
            self.fuel -= amount

    def dump(self):
        """Resets contents and fuel of the Jetpack to empty"""
        self.contents = []
        self.fuel = 0

# Problem 4: Write a 'ComplexNumber' class.
class ComplexNumber():
    """doc string placeholder"""

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def conjugate(self):
        self.img = -1 * self.img

    def __str__(self):
        """Returns the string of an object"""
        if self.img >= 0:
            return (f"{self.real} + {self.img}i")
        if self.img < 0:
            return (f"{self.real} - {self.img}i")
        
    def __abs__(self):
        return sqrt(self.real**2 + self.img**2)
    
    def __eq__(self, other):
        return self.real == other.real and self.img == other.img
    
    def __add__(self, other):
        return (f"{self.real + other.real} + {self.img + other.img}i")
    
    def __sub__(self, other):
        return (f"{self.real - other.real} + {self.img - other.img}i")
    
    def __mul__(self, other):
        return (f"{self.real * other.real} + {self.img * other.img}i")
    
    def __truediv__(self, other):
        return (f"{self.real / other.real} + {self.img / other.img}i")

def test_backpack():
    testpack = Backpack("Barry", "black")       # Instantiate the object.
    if testpack.name != "Barry":                # Test an attribute.
        print("Backpack.name assigned incorrectly")
    for item in ["pencil", "pen", "paper", "computer"]:
        testpack.put(item)                      # Test a method.
    print("Contents:", testpack.contents)

if __name__ == "__main__":
    test_backpack()