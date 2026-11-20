# Import Python's built-in unittest module.
# A module is a Python file or library containing reusable code.
# unittest provides tools for writing and running automated tests.
import unittest


# Define a class named TestPythonBasics.
# A class groups related data and behavior.
# The word "class" is a Python keyword used to define a class.
# TestPythonBasics is the name we have chosen for this class.
# unittest.TestCase provides built-in testing functionality.
# The parentheses indicates that our class inherits from TestCase.
# The colon (") begins the intended class body.
class TestPythonBasics(unittest.TestCase):

    # Define a method named test_addition.
    # "def" is the Python keyword for defining a function or method.
    # The name starts with "test_" so unittest can discover it.
    # "self" refers to the current instance of TestPythonBasics.
    # The colon (:) begins the intended method body.
    def test_addition(self):

        # Create a variable named result.
        # The equal sign (=) assigns the value to the variable.
        # Python evaluates 10 + 20 before assigning the result.
        # Therefore, result contains the integer 30.
        result = 10 + 20

        # Call the assertEqual method provided by unittest.TestCase.
        # "self" gives us access to that inherited method.
        # The first argument, result, is the actual calculated value.
        # The second argument, 30, is the expected value.
        # If both values are equal, the assertion passes.
        # If they differ, unittest records a test failure.
        self.assertEqual(result, 30)