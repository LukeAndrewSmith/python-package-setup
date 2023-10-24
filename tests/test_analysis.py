import unittest

from analysis.analyse_data import calculate_mean


class TestSimple(unittest.TestCase):
    def test_calculate_mean(self):
        self.assertEqual(calculate_mean(), 2)


if __name__ == "__main__":
    unittest.main()
