from assignments import MaxSizeList
import unittest

class MaxSizeListTest(unittest.TestCase):

    def setUp(self):
        self.a = MaxSizeList(3)
        self.b = MaxSizeList(1)

    def test_stores_1_elements(self):
        self.a.push("hey")
        self.assertEqual(["hey"], self.a.get_list())

    def test_stores_only_till_limit(self):
        self.a.push("hey")
        self.a.push("hi")
        self.a.push("lets")
        self.a.push("go")
        self.assertEqual(["hi", "lets", "go"], self.a.get_list())
