# The learner has reached for a plain unittest assertion rather than an
# approval, which is a failure rather than an error, and the lambda names
# both as red.
from hiker import answer
import unittest


class TestHiker(unittest.TestCase):

    def test_life_the_universe_and_everything(self):
        self.assertEqual(42, answer())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
