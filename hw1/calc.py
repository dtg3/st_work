import unittest

def evaluate_single_digit(s):
    i = "0123456789".index(s)
    return i

def evaluate_positive_number(s):
    n = 0
    for c in s:
        d = evaluate_single_digit(c)
        n = n * 10 + d
    return n

def evaluate_floating_point_number(s):
    in_decimal = False
    n = 0
    v = 0.1
    for c in s:
        if c == '.':
            if in_decimal:
                raise ValueError("Can't have two decimal points in one number")
            else:
                in_decimal = True
            continue
        if not in_decimal:
            d = evaluate_single_digit(c)
            n = n * 10 + d
        else:
            d = evaluate_single_digit(c)
            n = n + d * v
            v = v / 10
    return n

def evaluate_single_hex(s):
    return "0123456789ABCDEF".index(s)

def evaluate(s):
    if s.startswith("-"):
        return evaluate(s[1:]) * -1
    if s.startswith("0x"):
        return evaluate_single_hex(s[2:])
    return evaluate_floating_point_number(s)

class Test_000_Calculator(unittest.TestCase):

    def test_single_digit(self):
        i = 0
        for c in '0123456789':
            self.assertEqual(evaluate(c),i)
            i = i + 1

    def test_multiple_digits(self):
        self.assertEqual(evaluate('99999'),99999)
        self.assertEqual(evaluate('12345'),12345)
        self.assertEqual(evaluate('99999'),99999)
        self.assertEqual(evaluate('99'),99)
        self.assertEqual(evaluate('00'),00)

    def test_negative_numbers(self):
        self.assertEqual(evaluate('-123'),-123)
        self.assertEqual(evaluate('-1'),-1)
        self.assertEqual(evaluate('0'),0)
        self.assertEqual(evaluate('---123'),-123)

    def test_floating_numbers(self):
        self.assertEqual(evaluate('123.456'),123.456)
        self.assertEqual(evaluate('-123.456'),-123.456)

    def test_single_hex_to_decimal(self):
        i = 0
        for c in '0123456789ABCDEF':
            self.assertEqual(evaluate('0x' + c), i)
            i += 1

    def test_multiple_hex_to_decimal(self):
        self.assertEqual(evaluate('0x00'), 0)




if __name__ == "__main__":
    unittest.main()
