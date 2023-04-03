import unittest
from function import info


class NamesTestCase(unittest.TestCase):

    def test_name_function(self):
        full_name = info()
        self.assertEqual(full_name, '小把-18')


unittest.main()
