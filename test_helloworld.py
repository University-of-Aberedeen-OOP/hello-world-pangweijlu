import unittest
from helloworld import *


class Test_helloworld(unittest.TestCase):

    def test_helloworld(self):
        self.assertEqual(say_hello(),"hello world!", "not the expected output")



if __name__ == '__main__':
    unittest.main()