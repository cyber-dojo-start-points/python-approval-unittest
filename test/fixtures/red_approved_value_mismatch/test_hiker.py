# The approved value and the value the code produces differ. ApprovalTests
# raises for the mismatch, so unittest counts it as an error rather than a
# failure, and the lambda names errors as red.
from hiker import answer
import unittest
from approvaltests.approvals import verify
from approvaltests.reporters.report_on_cyber_dojo import ReportOnCyberDojo
from approvaltests import set_default_reporter


class TestHiker(unittest.TestCase):
    def setUp(self):
        set_default_reporter(ReportOnCyberDojo())

    def test_life_the_universe_and_everything(self):
        verify(str(answer()))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
