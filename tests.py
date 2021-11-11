import unittest
import main


class TestAboveBelow(unittest.TestCase):

    def test_normal_list(self):
        li: list = [1, 2, 3, 4, 5, 6]
        comparison_value: int = 3
        self.assertEqual(main.above_below(li, comparison_value), {'above': 3, 'below': 2})

    def test_not_in_list(self):
        li: list = [1, 2, 3, 4, 5, 6]
        comparison_value: int = 0
        self.assertEqual(main.above_below(li, comparison_value), {'above': None, 'below': None})

    def test_normal_sting(self):
        string: str = 'MyString'
        rotation: int = 2
        self.assertEqual(main.string_rotation(string, rotation), "ngMyStri")

    def test_large_rotation(self):
        string: str = 'MyString'
        rotation: int = 190156
        self.assertEqual(main.string_rotation(string, rotation), "ringMySt")


if __name__ == '__main__':
    unittest.main()