# cyber-dojo.sh hands unittest the files matching *test*.py, a glob that looks
# in the sandbox dir only, so a test file in a sub-dir is never run, and mypy
# and coverage do not reach into the sub-dir either, so it leaves no trace in
# the output at all. The assertion is a plain one that would fail, so a green
# says it really did not run rather than that it ran and passed.
from hiker import answer
import unittest


class TestAnswerSize(unittest.TestCase):

    def test_the_answer_is_three_digits_long(self):
        self.assertEqual(3, len(str(answer())))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
