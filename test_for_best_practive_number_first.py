import unittest

from best_practice_number_first import функция_которая_возвращает_когото, функция_номер_два


class TestBestPracticeNumberFirst(unittest.TestCase):
    def test_first_practice(self):
        self.assertEqual(функция_которая_возвращает_когото([1, 2, 3], [123124, "ежик"], 4), [246248, '123124ежик123124ежик123124ежик123124ежик', 'ежик123124ежик123124ежик123124ежик123124'])
    def test_second_practice(self):
        self.assertEqual(функция_номер_два(), None)