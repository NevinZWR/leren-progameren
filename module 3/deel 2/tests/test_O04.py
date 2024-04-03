import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import *

#schrijf je test hier
def test_journey_duration():
    assert JOURNEY_IN_DAYS == 11

if __name__ == "__main__":
    test_journey_duration()
    print("All tests pass.")