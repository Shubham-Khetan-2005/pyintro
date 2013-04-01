import unittest
import calc


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = calc.Calculator()

    def test_sum(self):
        expected = 7
        got = self.calc.sum(2, 5)
        self.assertEqual(expected, got, '2 + 5 should be equal to 7')
