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
        """Test case 1 using test_empty.txt."""
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
            'Ramayana: The Legend of Prince Rama', 100)
        expected_result = ['Spirited Away',
                           'Meiji Tokyo Renka Movie: Yumihari no Serenade',
                           'Natsu e no tunnel, Sayonara no deguchi',
                           'Attack on Titan: Chronicle', 'Gintama: The Final',
                           'Grave of the Fireflies',
                           'Attack on Titan: The Roar of Awakening',
                           'Your Name.', 'Princess Mononoke', 'Fresh Precure!',
                           'Gintama the Movie: The Final Chapter - Be Forever Yorozuya',
                           'Gaiking II', 'Precure Allstars DX',
                           'From the Apennines to the Andes: The Movie',
                           "Conan the Future Boy: The Big Giant Robot's Resurrection",
                           'Gekijouban Shimajirou no wao!: Shimajirou to kujira no uta',
                           'Magnetic Rose',
                           'Demon Slayer the Movie: Mugen Train',
                           'Rascal Does Not Dream of a Dreaming Girl',
                           "Howl's Moving Castle", 'Makoto-chan',
                           'Tistou the Green Thumb',
                           'A Silent Voice: The Movie', 'Wolf Children',
                           'Legend of the Galactic Heroes: Die Neue These - Stellar War 3',
                           'Shoujo Kageki Revue Starlight: Rondo Rondo Rondo',
                           'Girls und Panzer Compilation Movie',
                           'Made in Abyss: Dawn of the Deep Soul',
                           'My Neighbor Totoro', 'Zoku Owarimonogatari',
                           "Fate/stay night [Heaven's Feel] II. lost butterfly",
                           'I Want to Eat Your Pancreas',
                           'Mobile Suit Gundam: The Origin III - Dawn of Rebellion',
                           'Black Butler: Book of Murder',
                           'Kizumonogatari Part 3: Reiketsu',
                           'Slam Dunk: Zenkoku Seiha da! Sakuragi Hanamichi',
                           'Deadstar the Movie',
                           'The Tale of The Princess Kaguya',
                           'Evangelion: 3.0+1.01 Thrice Upon a Time',
                           'Puella Magi Madoka Magica the Movie Part 2: Eternal',
                           'The Disappearance of Haruhi Suzumiya',
                           'The Quintessential Quintuplets Movie',
                           'Eiga Yurukyan',
                           'Gurren Lagann the Movie: The Lights in the Sky are Stars',
                           'Revue Starlight the Movie',
                           'The Garden of Sinners: Paradox Spiral',
                           'Neon Genesis Evangelion: The End of Evangelion',
                           'Perfect Blue', 'Akira', 'Castle in the Sky',
                           'Nausicaä of the Valley of the Wind',
                           'Barefoot Gen',
                           "Konosuba!: God's Blessing on This Wonderful World! - Legend of Crimson",
                           "Fate/stay night [Heaven's Feel] III. spring song",
                           "JoJo's Bizarre Adventure: Phantom Blood",
                           'Kuroko No Basket Movie 3: Winter Cup Soushuuhen - Tobira No Mukou',
                           'Gekijôban Shingeki no Kyojin Kôhen: Jiyû no tsubasa',
                           'Ushiro no shoumen daare', 'Ghost in the Shell 2.0',
                           'Evangelion: 2.0 You Can', 'Whisper of the Heart',
                           'Ghost in the Shell',
                           'Legend of the Galactic Heroes: Overture to a New War',
                           'Conan, the Boy in Future',
                           'Dragon Ball Super: Broly',
                           'Kuroko no Basket Movie 1: Winter Cup Soushuuhen - Kage to Hikari',
                           'Ajin Part 2: Shoutotsu',
                           'Boruto: Naruto The Movie',
                           'Steins;Gate: The Movie - Load Region of Déjà Vu',
                           'Puella Magi Madoka Magica the Movie Part III: The Rebellion Story',
                           'One Piece Film Z',
                           'Berserk: The Golden Age Arc III - The Advent',
                           'To the Forest of Firefly Lights',
                           'Jujutsu Kaisen 0: The Movie',
                           'Revival of Evangelion',
                           'High School Fleet the Movie',
                           'Sword of the Stranger',
                           'My Hero Academia: Heroes Rising',
                           'Shining Star: The Birth of New Luna-Queen',
                           'Made in Abyss: Wandering Twilight',
                           'Detective Conan: The Phantom of Baker Street',
                           'Inochi no chikyuu: Daiokishin no natsu',
                           'Tokyo Godfathers',
                           'Interstella 5555: The 5tory of the 5ecret 5tar 5ystem',
                           'Cardcaptor Sakura: The Sealed Card',
                           'Millennium Actress', 'Cowboy Bebop: The Movie',
                           'Ninja Scroll', "Kiki's Delivery Service",
                           'Legend of the Galactic Heroes: My Conquest is the Sea of Stars',
                           'Mobile Suit Gundam: The Origin VI - Rise of the Red Comet',
                           'Princess Principal Crown Handler: Chapter 1',
                           'Mobile Suit Gundam: The Origin V - Clash at Loum',
                           "Kuroko's Basketball: Last Game",
                           'Mobile Suit Gundam: The Origin IV - Eve of Destiny',
                           'Dou Kyu Sei: Classmates',
                           'The Shimajiro Movie: Shimajiro in Bookland',
                           'In This Corner', 'Asatte Dansu']
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
