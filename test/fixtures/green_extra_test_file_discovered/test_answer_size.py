from hiker import answer
import unittest
from approvaltests.approvals import verify
from approvaltests.reporters.report_on_cyber_dojo import ReportOnCyberDojo
from approvaltests import set_default_reporter


class TestAnswerSize(unittest.TestCase):
    def setUp(self):
        set_default_reporter(ReportOnCyberDojo())

    def test_the_answer_is_two_digits_long(self):
        verify(str(len(str(answer()))))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
