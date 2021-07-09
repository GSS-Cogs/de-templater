from enum import Enum
import unittest

from detemplater.allquestions import QUESTION_SUITES
from detemplater.validation import validate_step
from detemplater.models import DbParadime

# No point listifying the same enums over and over again
DB_PARADIMES_AS_LIST = [x.value for x in DbParadime]
class TestValidation(unittest.TestCase):

    # Test that validation correctly identifies where
    # a databaker paradime has been incorrectly added
    def test_invalid_step_supperflous_input(self):

        paradimes_as_list = [x.value for x in DbParadime]

        class FakeDbParadime(Enum):
            thing1 = paradimes_as_list[0]
            thing2 = paradimes_as_list[1]
            thing3 = paradimes_as_list[2]
            thing4 = "im not supposed to be here"

        relevant_question = QUESTION_SUITES['v1_basic'][2]

        with self.assertRaises(Exception) as context:
            validate_step(relevant_question, enum_dict = {"DbParadime": FakeDbParadime})

        self.assertTrue('has unexpected inputs defined.' in str(context.exception))


    # Test that validation correctly identifies where
    # a definition has changed
    def test_invalid_step_supperflous_input(self):

        paradimes_as_list = [x.value for x in DbParadime]

        class FakeDbParadime(Enum):
            thing1 = paradimes_as_list[0]
            thing2 = paradimes_as_list[1]
            thing3 = paradimes_as_list[2]+'I am totally wrong'

        relevant_question = QUESTION_SUITES['v1_basic'][2]

        with self.assertRaises(Exception) as context:
            validate_step(relevant_question, enum_dict = {"DbParadime": FakeDbParadime})

        self.assertTrue('has unexpected inputs defined.' in str(context.exception))


if __name__ == '__main__':
    unittest.main()