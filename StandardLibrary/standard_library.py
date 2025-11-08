# standard_library.py
"""Python Essentials: The Standard Library.
Ellison Hall
Math Clinic 
November 8, 2025
"""

from math import sqrt


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    return min(L), max(L), sum(L)/len(L)
    raise NotImplementedError("Problem 1 Incomplete")

if __name__ == "__main__": 
    print(prob1([1, 2, 3, 4, 5]))

# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    inte = 5
    stri = "strings"
    lis = [1, 2, 2, 3 ,4 ,5]
    tup = (1,2,3)
    se ={1, 2, 2, 3, 4, 5}

    """Assign new"""
    inte1 = inte
    stri1 = stri
    lis1 = lis
    tup1 = tup
    se1 = se

    """New Changes"""
    inte1 += 1
    stri1 += "!"
    lis1.append(6)
    se1.add(6)
    
    """If they are mutable"""
    print("int mutable?", inte == inte1)
    print("string mutable?", stri == stri1)
    print("list mutable?", lis == lis1)
    print("tuple mutable?", tup == tup1)
    print("set mutable?", se == se1)
    return ()
    raise NotImplementedError("Problem 2 Incomplete")

if __name__ == "__main__": 
    print(prob2())

# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt() that are
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    raise NotImplementedError("Problem 5 Incomplete")
