import unittest
from palindrome import palindrome

class TestPalindrome(unittest.TestCase):

    def setUp(self):

        self.phrases = [
            "нажал кабан на баклажан",
            "дом как комод",
            "рвал дед лавр",
            "азот калий и лактоза",
            "а собака боса",
            "тонет енот",
            "карман мрак",
            "пуст суп",
            "а роза упала на лапу азора"
        ]

    def test_palindrome(self):
        self.assertEqual(palindrome(self.phrases), ['нажал кабан на баклажан', 'рвал дед лавр',
                                              'азот калий и лактоза', 'а собака боса', 'тонет енот',
                                              'пуст суп', 'а роза упала на лапу азора'])

