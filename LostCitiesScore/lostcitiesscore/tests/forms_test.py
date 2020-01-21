import pytest
from django.forms import Form
from lostcitiesscore import forms



TEST_SCORES = [
    ({
        'cards_A_round_1': 'dd23',
        'cards_B_round_1': 'dd23',
        'cards_A_round_2': 'dd23',
        'cards_B_round_2': 'dd23',
        'cards_A_round_3': 'dd23',
        'cards_B_round_3': 'dd23',
    }, True),
]



def test_can_init_form():
    form = forms.IndexForm()

    assert isinstance(form, Form)
    assert not form.is_bound



def test_accepts_player_round_data():
    data = {
        'p1r1': 'a',
        'p2r1': 'a',
        'p1r2': 'a',
        'p2r2': 'a',
        'p1r3': 'a',
        'p2r3': 'a',
    }
    form = forms.IndexForm(data=data)

    assert form.is_bound



def test_form_has_fields():
    fields = (
        'cards_A_round_1',
        'cards_B_round_1',
        'cards_A_round_2',
        'cards_B_round_2',
        'cards_A_round_3',
        'cards_B_round_3',
    )
    form = forms.IndexForm()

    assert tuple(form.fields.keys()) == fields




@pytest.mark.parametrize('data, expected', TEST_SCORES)
def test_form_validation(data, expected):
    form = forms.IndexForm(data={
        'cards_A_round_1': '2',
        'cards_B_round_1': '2',
        'cards_A_round_2': '2',
        'cards_B_round_2': '2',
        'cards_A_round_3': '2',
        'cards_B_round_3': '2',
    })

    # print(form.fields.keys())
    # print(help(form))
    print(form.errors)

    assert form.is_valid() == expected
