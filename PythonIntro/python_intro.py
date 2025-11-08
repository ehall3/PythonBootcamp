# python_intro.py
"""Python Essentials: Introduction to Python.
Ellison Hall
Math Clinic
November 8, 2025
"""


# Problem 1 (write code below)
if __name__ == "__main__":
    print("Hello, world!")

# Problem 2
def sphere_volume(r):
    """ Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
    volume = (4/3)*(3.1415)*(r**3)
    return volume
    raise NotImplementedError("Problem 2 Incomplete")

if __name__ == "__main__":
    print(sphere_volume(2))

# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    return (a,"     " + str(b) + "     ", c, d, e)
    raise NotImplementedError("Problem 3 Incomplete")

if __name__ == "__main__":
    print(isolate(1, 2, 3, 4, 5))

# Problem 4
def first_half(my_string):
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """

    l = len(my_string)
    l = l//2
    return my_string[:l]
    raise NotImplementedError("Problem 4 Incomplete")

if __name__ == "__main__":
    print(first_half("python"))

def backward(my_string):
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
    l = len(my_string)
    return my_string[::-1]
    raise NotImplementedError("Problem 4 Incomplete")

if __name__ == "__main__":
    print(backward("python"))

# Problem 5
def list_ops():
    """ Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.

    Examples:
        >>> list_ops()
        ['fox', 'hawk', 'dog', 'bearhunter']
    """

    animals = ["bear", "ant", "cat", "dog"]
    animals.append("eagle")
    animals[2] = "fox"
    animals.pop(1)
    animals.sort(reverse=True)
    eagle_index = animals.index("eagle")
    animals[eagle_index] = "hawk"
    animals[-1] = animals[-1] + "hunter"
    return animals
    raise NotImplementedError("Problem 5 Incomplete")

if __name__ == "__main__":
    print(list_ops())

# Problem 6
def pig_latin(word):
    """ Translate the string 'word' into Pig Latin, and return the new word.

    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """

    vowels = "aeiou"
    if word[0].lower() in vowels:
        return word + "hay"
    else:
        return word[1:] + word[0] + "ay"
    raise NotImplementedError("Problem 6 Incomplete")

if __name__ == "__main__":
    print(pig_latin("apple"))

# Problem 7
def palindrome():
    """ Find and retun the largest panindromic number made from the product
    of two 3-digit numbers.
    """
    largest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if str(product) == str(product)[::-1]:  # check palindrome
                if product > largest:
                    largest = product
    return largest
    raise NotImplementedError("Problem 7 Incomplete")

if __name__ == "__main__":
    print(palindrome())

# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    total = 0
    for k in range(1, n + 1):
        total += ((-1) ** (k + 1)) * (1 / k)
    return total
    raise NotImplementedError("Problem 8 Incomplete")

if __name__ == "__main__":
    print(alt_harmonic(1))