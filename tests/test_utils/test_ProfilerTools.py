import io
from time import sleep
from unittest.mock import patch  # TODO: Switch to pytest mocking

from mttools.utils.ProfilerTools import *


class TestTimer:
    @staticmethod
    @Timer(unit="s")
    def sleep_half_s():
        sleep(0.5)

    @staticmethod
    @Timer(unit="min", message="Do Nothing Function")
    def do_nothing():
        pass

    @staticmethod
    @Timer(unit="Bad Unit")
    def do_nothing_bad_unit():
        pass

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_sleep_half_sec(self, mock_stdout):
        self.sleep_half_s()
        result = mock_stdout.getvalue()
        time_elapsed = float(result[-7:-3])
        unit = result[-2:-1]
        assert 0.5 == time_elapsed
        assert "s" == unit

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_message_and_unit(self, mock_stdout):
        self.do_nothing()
        result = mock_stdout.getvalue()
        assert "\n\nTime Elapsed: 0.000min\n\tDo Nothing Function\n" == result

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_bad_unit(self, mock_stdout):
        self.do_nothing_bad_unit()
        result = mock_stdout.getvalue()
        expected = (
            "\n\nBad unit given to @timer, Valid units are:"
            "\n\tns, us, ms, s, min"
            "\n\tUsing default ms\n"
        )
        assert (
            expected == result[:-24]
        )  # Only testing error message due to unpredictability in time elapsed
