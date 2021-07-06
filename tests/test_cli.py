import os
from pathlib import Path
from random import randint
from subprocess import run, PIPE
import unittest

class TestCli(unittest.TestCase):
    """
    Test that when called 100 times with only integer 1-10 choices being
    made no exceptions are encountered.
    """

    # Test that unexpected inputs do NOT break the cli.
    # Note: runs 100 iterations of random selections looking for an
    # uncontrolled error (i.e an uber primitive chaos monkey).
    def test_cli_accepts_any_integers(self): 

        mock_run_counter = 0
        this_scripts_dir = Path(os.path.dirname(os.path.realpath(__file__)))
        cli_path = Path(this_scripts_dir.parent / "detemplater")

        while mock_run_counter < 100:

            # We'll get 200 inputs, that should be statistically bullet proof
            # for our half dozen questions with approx 1/4 chance of having
            # to answer twice for out of range.
            inputs_list = [str(randint(1,5)) for x in range(200)]

            p = run(['python3', f'{cli_path}/cli.py'], stdout=PIPE, input="\n".join(inputs_list), encoding='ascii')
            print(p)

            mock_run_counter += 1


if __name__ == '__main__':
    unittest.main()
        

