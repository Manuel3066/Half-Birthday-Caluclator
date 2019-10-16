import unittest
from function import birtdhay_calculator
import datetime

class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        test_date = datetime.datetime(2019, 4, 22)
        self.assertEqual(birtdhay_calculator.half_birtday(test_date), test_date+datetime.timedelta(days=182))


if __name__ == '__main__':
    unittest.main()
