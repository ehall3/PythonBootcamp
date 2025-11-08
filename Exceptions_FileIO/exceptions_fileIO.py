# exceptions_fileIO.py
"""Python Essentials: Exceptions and File Input/Output.
Ellison Hall
Math Clinic
November 8, 2025
"""

from random import choice


# Problem 1
def arithmagic():
    """
    Takes in user input to perform a magic trick and prints the result.
    Verifies the user's input at each step and raises a
    ValueError with an informative error message if any of the following occur:

    The first number step_1 is not a 3-digit number.
    The first number's first and last digits differ by less than $2$.
    The second number step_2 is not the reverse of the first number.
    The third number step_3 is not the positive difference of the first two numbers.
    The fourth number step_4 is not the reverse of the third number.
    """

    step_1 = input("Enter a 3-digit number where the first and last "
                                           "digits differ by 2 or more: ")
    if len(step_1) != 3:
        raise ValueError("The input has to be a three digit number")
    
    if abs(int(step_1[2]) - int(step_1[0])) < 2:
        raise ValueError("First and last digits must have a differnce greater than 2")

    step_2 = input("Enter the reverse of the first number, obtained "
                                              "by reading it backwards: ")
    
    if step_2[::-1] != step_1:
        raise ValueError("The second number is not a reverse of the first")
    
    step_3 = input("Enter the positive difference of these numbers: ")

    if step_3 != abs(int(step_1) - int(step_1)):
        raise Exception("The third number is not a positive difference of the first two numbers.")
    
    step_4 = input("Enter the reverse of the previous result: ")

    if step_4 != step_3[::-1]:
        raise ValueError("The fourth number is not the reverse of the thrid number.")
    
    print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")


# Problem 2
def random_walk(max_iters=1e12):
    """
    If the user raises a KeyboardInterrupt by pressing ctrl+c while the
    program is running, the function should catch the exception and
    print "Process interrupted at iteration $i$".
    If no KeyboardInterrupt is raised, print "Process completed".

    Return walk.
    """
    walk = 0
    directions = [1, -1]
    try:
        for i in range(int(max_iters)):
            walk += choice(directions)
    except KeyboardInterrupt:
        print(f"Process Interupted at iteration {i}")
    else:
        print("Process Completed")
    return print(walk, i) 


# Problems 3 and 4: Write a 'ContentFilter' class.
class ContentFilter():
    """Class for reading in file

    Attributes:
        filename (str): The name of the file
        contents (str): the contents of the file

    """

    # Problem 3
    def __init__(self, filename):
        """ Read from the specified file. If the filename is invalid, prompt
        the user until a valid filename is given.
        """
        self.filename = filename

        KeepTrying = True
        while KeepTrying:
            try: 
                with open(filename, 'r') as myfile:
                    self.contents = myfile.read()
                    KeepTrying = False
            except (FileNotFoundError, TypeError, OSError, ValueError, NameError) as e:
                self.filename = input("Please input a valid filename: ")
                myfile.close
            else:
             KeepTrying = False

        with open(filename, 'r') as myfile:
            self.contents = myfile.read()
            self.filename = filename

 # Problem 4 ---------------------------------------------------------------
    def check_mode(self, mode):
        """ Raise a ValueError if the mode is invalid. """

    def uniform(self, outfile, mode='w', case='upper'):
        """ Write the data to the outfile with uniform case. Include a
        keyword argument case that defaults to "upper". If case="upper", write
        the data in upper case. If case="lower", write the data in lower case.
        If case is not one of these two values, raise a ValueError. """


    def reverse(self, outfile, mode='w', unit='line'):
        """ Write the data to the outfile in reverse order. Include a
        keyword argument unit that defaults to "line". If unit="word", reverse
        the ordering of the words in each line, but write the lines in the same
        order as the original file. If units="line", reverse the ordering of the
        lines, but do not change the ordering of the words on each individual
        line. If unit is not one of these two values, raise a ValueError. """

    def transpose(self, outfile, mode='w'):
        """ Write a transposed version of the data to the outfile. That is, write
        the first word of each line of the data to the first line of the new file,
        the second word of each line of the data to the second line of the new
        file, and so on. Viewed as a matrix of words, the rows of the input file
        then become the columns of the output file, and viceversa. You may assume
        that there are an equal number of words on each line of the input file. """

    def __str__(self):
        """ Printing a ContentFilter object yields the following output:

        Source file:            <filename>
        Total characters:       <The total number of characters in file>
        Alphabetic characters:  <The number of letters>
        Numerical characters:   <The number of digits>
        Whitespace characters:  <The number of spaces, tabs, and newlines>
        Number of lines:        <The number of lines>
        """

if __name__ == "__main__":
    ContentFilter('out.txt')