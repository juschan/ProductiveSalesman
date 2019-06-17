import unittest

def square(x):
    return x*x

class TestSquare(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(2),4)

if __name__ == '__main__':
    unittest.main()