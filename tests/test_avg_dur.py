"""Test Average Duration for a given Genre."""

import os
import unittest
from apps.anime import AnimeData


class TestAverageGross(unittest.TestCase):
    """Test `test_avg_gross()` method."""

    def setUp(self):
        """Create AnimeData objects for the four testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.empty = AnimeData(f'{data_dir}/test_empty.txt')
        self.starting5 = AnimeData(f'{data_dir}/test_first_data.txt')
        self.ending5 = AnimeData(f'{data_dir}/test_last_data.txt')
        self.full = AnimeData(f'{data_dir}/top_100_anime_LIST.csv')

    def test_empty(self):
        """Test case 1 using test_empty.txt."""
        actual_result = self.empty.avg_genre_dur('Action')
        expected_result = 0.0
        self.assertEqual(actual_result, expected_result)

    def test_first_data(self):
        """Test case 2 using test_first_data.txt."""
        actual_result = self.starting5.avg_genre_dur('Action')
        expected_result = 109.5
        self.assertEqual(actual_result, expected_result)

    def test_last_data(self):
        """Test case 3 using test_last_data.txt."""
        actual_result = self.ending5.avg_genre_dur('Music')
        expected_result = 60
        self.assertEqual(actual_result, expected_result)

    def test_full(self):
        """Test case 4 using top_100_anime_LIST.csv."""
        actual_result = self.full.avg_genre_dur('Romance')
        expected_result = 52.5
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
