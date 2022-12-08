"""Test Recommendation."""

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
        actual_result = self.empty.recommended_anime(
            'Ramayana: The Legend of Prince Rama', 1)
        expected_result = []
        self.assertListEqual(actual_result, expected_result)

    def test_first_data(self):
        """Test case 2 using test_first_data.txt."""
        actual_result = self.starting5.recommended_anime(
            'Ramayana: The Legend of Prince Rama', 1)
        expected_result = ['Spirited Away']
        self.assertListEqual(actual_result, expected_result)

    def test_last_data(self):
        """Test case 3 using test_last_data.txt."""
        actual_result = self.ending5.recommended_anime('Incorrect Name', 1)
        expected_result = []
        self.assertEqual(actual_result, expected_result)

    def test_full(self):
        """Test case 4 using top_100_anime_LIST.csv."""
        actual_result = self.full.recommended_anime(
            'Ramayana: The Legend of Prince Rama', 10)
        expected_result = ['Spirited Away',
                           'Meiji Tokyo Renka Movie: Yumihari no Serenade',
                           'Natsu e no tunnel, Sayonara no deguchi',
                           'Attack on Titan: Chronicle', 'Gintama: The Final',
                           'Grave of the Fireflies',
                           'Attack on Titan: The Roar of Awakening',
                           'Your Name.', 'Princess Mononoke', 'Fresh Precure!']
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
