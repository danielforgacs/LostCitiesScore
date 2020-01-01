import os
import sys
import pytest

ROOTDIR = (
    os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
)))

sys.path = [ROOTDIR] + sys.path

import LostCitiesScore.scorecounter as counter


SCORE_TEXTS = [
    ['281', 0],
    ['281;281', 0],
    ['281;281;281;281', 0],
    ['d281;281;281;281', 0],
    ['d281;d281;d281;281', 0],

    ['381', 1],
    ['d381', 2],
]


@pytest.mark.parametrize('txt, expected', SCORE_TEXTS)
def test_score_counter(txt, expected):
    assert counter.main(text=txt) == expected
