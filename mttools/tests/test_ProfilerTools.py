import unittest
import io
from unittest.mock import patch
from time import sleep
from ProfilerTools import *


class TestTimer(unittest.TestCase):

    @staticmethod
    @Timer(unit='s')
    def sleep_half_s():
        sleep(.5)

    @staticmethod
    @Timer(unit='min', message="Do Nothing Function")
    def do_nothing():
        pass

    @staticmethod
    @Timer(unit='Bad Unit')
    def do_nothing_bad_unit():
        pass

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sleep_half_sec(self, mock_stdout):
        self.sleep_half_s()
        result = mock_stdout.getvalue()
        time_elapsed = float(result[-7:-3])
        unit = result[-2:-1]
        self.assertEqual(.5, time_elapsed)
        self.assertEqual('s', unit)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_message_and_unit(self, mock_stdout):
        self.do_nothing()
        result = mock_stdout.getvalue()
        self.assertEqual("\n\nTime Elapsed: 0.000min\n\tDo Nothing Function\n", result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_unit(self, mock_stdout):
        self.do_nothing_bad_unit()
        result = mock_stdout.getvalue()
        expected = ("\n\nBad unit given to @timer, Valid units are:"
                    "\n\tns, us, ms, s, min"
                    "\n\tUsing default ms\n")
        self.assertEqual(expected, result[:-24])  # Only testing error message due to unpredictability in time elapsed


if __name__ == '__main__':
    unittest.main()
