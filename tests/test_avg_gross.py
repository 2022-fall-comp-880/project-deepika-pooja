"""Test Average gross in the given period."""

import os
import unittest
from apps.anime import AnimeData


class TestAverageGross(unittest.TestCase):
    """Test `test_avg_gross()` method."""

    def setUp(self):
        data_dir = os.path.dirname(__file__) + "/../data"
        self.empty = AnimeData(f'{data_dir}/test_empty.txt')
        self.starting5 = AnimeData(f'{data_dir}/test_first_data.txt')
        self.ending5 = AnimeData(f'{data_dir}/test_last_data.txt')
        self.full = AnimeData(f'{data_dir}/top_100_anime_LIST.csv')

    def test_empty(self):
        """Test case 1 using test_first.txt."""
        actual_result = self.empty.gross_avg([2022])
        expected_result = 0.0
        self.assertEqual(actual_result, expected_result)

    def test_first_data(self):
        """Test case 2 using test_first_data.txt."""
        actual_result = self.starting5.gross_avg([2020, 2021, 2022])
        expected_result = 19.41
        self.assertEqual(actual_result, expected_result)

    def test_last_data(self):
        """Test case 3 using test_last_data.txt."""
        actual_result = self.ending5.gross_avg([2016])
        expected_result = 3.79
        self.assertEqual(actual_result, expected_result)

    def test_full(self):
        """Test case 4 using top_100_anime_LIST.csv."""
        actual_result = self.full.gross_avg([2000])
        expected_result = 4.45
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
