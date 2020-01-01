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

    ['dd23578;7891;34567', 15+14+5],
    ['7891', 14],

    ['23578', 5],
    ['dd23578', 15],
    ['34567', 5],
]

COLOUR_TEXTS = [
    ['7891', 14],
    ['d7891', 14*2],
    ['dd7891', 14*3],

    ['2', -18],
    ['23', -20+2+3],
    ['234', -20+2+3+4],
    ['23456789', -20+2+3+4+5+6+7+8+9 +20],
    ['23456789', 24+20],
]


@pytest.mark.parametrize('txt, expected', SCORE_TEXTS)
def test_score_counter(txt, expected):
    assert counter.main(text=txt) == expected


@pytest.mark.parametrize('txt, expected', COLOUR_TEXTS)
def test_count_colour(txt, expected):
    assert counter.count_colour(scoretext=txt) == expected
