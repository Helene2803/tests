import unittest
from quadratic_equation import discriminant, solution

class TestQuadraticEquation(unittest.TestCase):

    def test_discriminant(self):

        params = (
            (1, 8, 15, 4),
            (1, -13, 12, 121),
            (-4, 28, -49, 0),
            (1, 1, 1, -3)
        )

        for i, (a, b, c, expected) in enumerate(params):
            with self.subTest(i):
                result = discriminant(a, b, c)
                self.assertEqual(result, expected)

    def test_solution(self):

        params = (
            (1, 8, 15, (-3, -5)),
            (1, -13, 12, (12, 1)),
            (-4, 28, -49, 3.5),
            (1, 1, 1, 'корней нет')
        )

        for i, (a, b, c, expected) in enumerate(params):
            with self.subTest(i):
                result = solution(a, b, c)
                self.assertEqual(result, expected)