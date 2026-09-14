from fizz_buzz import fizz_buzz
import unittest
from approvaltests.approvals import verify
from approvaltests.reporters.report_on_cyber_dojo import ReportOnCyberDojo
from approvaltests import set_default_reporter


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        set_default_reporter(ReportOnCyberDojo())

    def test_life_the_universe_and_everything(self):
        verify(str(fizz_buzz()))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
