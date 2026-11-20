import unittest

class TestPythonBasics(unittest.TestCase):
    """Basic tests for learning Python and unittest."""

    def test_addition(self):
        """Verify that addition produces the expected result."""

        # Calculate the actual result.
        result = 10 + 20

        # Compare the actual result with the expected value.
        self.assertEqual(result, 30)
