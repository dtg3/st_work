import unittest
import calc

class Test_000_Calculator(unittest.TestCase):

    def test_single_digit(self):
        i = 0
        for c in '0123456789':
            self.assertEqual(calc.evaluate(c),i)
            i = i + 1

    def test_multiple_digits(self):
        self.assertEqual(calc.evaluate('99999'),99999)
        self.assertEqual(calc.evaluate('12345'),12345)
        self.assertEqual(calc.evaluate('99999'),99999)
        self.assertEqual(calc.evaluate('99'),99)
        self.assertEqual(calc.evaluate('00'),00)

    def test_negative_numbers(self):
        self.assertEqual(calc.evaluate('-123'),-123)
        self.assertEqual(calc.evaluate('-1'),-1)
        self.assertEqual(calc.evaluate('0'),0)
        self.assertEqual(calc.evaluate('---123'),-123)

    def test_floating_numbers(self):
        self.assertEqual(calc.evaluate('123.456'),123.456)
        self.assertEqual(calc.evaluate('-123.456'),-123.456)

    def test_single_hex_to_decimal(self):
        i = 0
        for c in '0123456789ABCDEF':
            self.assertEqual(calc.evaluate('0x' + c), i)
            i += 1

    def test_multiple_hex_to_decimal(self):
        self.assertEqual(calc.evaluate('0x00'), 0)
        self.assertEqual(calc.evaluate('0xFF'), 255)

        self.assertEqual(calc.evaluate('0x0000000000000000000000000000000000000'), 0)
        self.assertEqual(calc.evaluate('0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'),
            356811923176489970264571492362373784095686655)

        self.assertEqual(calc.evaluate('0x1234567890'), 78187493520)
        self.assertEqual(calc.evaluate('0xABCDEF'), 11259375)

        self.assertEqual(calc.evaluate('0xA83F'), 43071)
        self.assertEqual(calc.evaluate('0x1AB5'), 6837)
        self.assertEqual(calc.evaluate('0x9D2C'), 40236)
        self.assertEqual(calc.evaluate('0xD6B4'), 54964)

if __name__ == "__main__":
    unittest.main()
