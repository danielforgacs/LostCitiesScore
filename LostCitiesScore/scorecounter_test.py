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
    ['28t', 0],
    ['281 281', 0],
    ['28t 28t', 0],
    ['281 281 281 281', 0],
    ['d281 281 281 281', 0],
    ['d281 d281 d281 281', 0],

    ['381', 1],
    ['d381', 2],

    ['dd23578 7891 34567', 15+14+5],
    ['dd23578 789t 34567', 15+14+5],
    ['7891', 14],
    ['789t', 14],

    ['23578', 5],
    ['dd23578', 15],
    ['34567', 5],
]

COLOUR_TEXTS = [
    ['7891', 14],
    ['d7891', 14*2],
    ['dd7891', 14*3],
    ['dd789t', 14*3],

    ['2', -18],
    ['23', -20+2+3],
    ['234', -20+2+3+4],
    ['23456789', -20+2+3+4+5+6+7+8+9 +20],
    ['23456789', 24+20],

    ['2345678', -20+2+3+4+5+6+7+8],
    ['23456789', -20+2+3+4+5+6+7+8+9+20],
    ['23456789', (-20+2+3+4+5+6+7+8+9)+20],
    ['d23456789', ((-20+2+3+4+5+6+7+8+9)*2)+20],
    ['dd23456789', ((-20+2+3+4+5+6+7+8+9)*3)+20],
    ['ddd23456789', ((-20+2+3+4+5+6+7+8+9)*4)+20],
    ['ddd2345678', ((-20+2+3+4+5+6+7+8)*4)+20],
    ['ddd23456', ((-20+2+3+4+5+6)*4)+20],
    ['ddd2345', ((-20+2+3+4+5)*4)],
]


@pytest.mark.parametrize('txt, expected', SCORE_TEXTS)
def test_score_counter(txt, expected):
    assert counter.main(text=txt) == expected



@pytest.mark.parametrize('goodvalue', (
    2, 3, 4, 5, 6, 7, 8, 9, 10
))
def test_Card_init(goodvalue):
    instance = counter.Card(value=goodvalue)
    instance.attr = goodvalue



@pytest.mark.parametrize('badvalue', (
    1, 11, '1', [1, 2], 1.23,
))
def test_Card_errors_on_bad_value(badvalue):

    with pytest.raises(ValueError):
        instance = counter.Card(value=badvalue)




def test_Card_has_value():
    card = counter.Card(value=2)
    assert hasattr(card, 'value')




@pytest.mark.parametrize('rowdata', COLOUR_TEXTS)
def test_Row_has_proper_value(rowdata):
    rowtxt, expected = rowdata
    row = counter.Row(scoretext=rowtxt)

    assert row.value == expected
