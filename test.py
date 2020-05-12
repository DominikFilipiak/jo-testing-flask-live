import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Tests that it can sum a list of integers
        :return:
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
        print('Chyba się udało!')


if __name__ == 'main':
    unittest.main()