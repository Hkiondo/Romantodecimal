#test_romanprac.py
import unittest
from romanprac import romanToDecimal

class TestRomanPrac(unittest.TestCase):
    def test_roman_to_number(self):
        self.assertEqual(romanToDecimal('III'), 3)
        self.assertEqual(romanToDecimal('IV'), 4)
        self.assertEqual(romanToDecimal('IX'), 9)
        self.assertEqual(romanToDecimal('LVIII'), 58)
        self.assertEqual(romanToDecimal('MCMXCIV'), 1994)

    def test_single_letters(self):
        self.assertEqual(romanToDecimal('I'),1)
        self.assertEqual(romanToDecimal('V'),5)
        self.assertEqual(romanToDecimal('X'),10)
        self.assertEqual(romanToDecimal('L'),50)
        self.assertEqual(romanToDecimal('C'),100)
        self.assertEqual(romanToDecimal('D'),500)
        self.assertEqual(romanToDecimal('M'),1000)
    
    def test_many_letters(self):
        self.assertEqual(romanToDecimal('XI'),11)

    def test_subractive_notation(self):
        self.assertEqual(romanToDecimal('IV'),4)

    def test_with_and_without_subractive_notation(self):
        self.assertEqual(romanToDecimal('XIV'),14)

    def test_repetition(self):
        self.assertEqual(romanToDecimal('II'),2)

    def test_first_number(self):
        self.assertEqual(romanToDecimal('I'),1)

    def test_roman_to_number_invalid(self):
        self.assertIsNone(romanToDecimal('IIII')) #Invalid since 4 should be represented as IV

    def test_invalid_and_valid_letter(self):
        self.assertIsNone(romanToDecimal('XIZ'))

if __name__ == '__main__':
    unittest.main()