from django.forms import Form
from lostcitiesscore import forms



def test_can_init_form():
    form = forms.IndexForm()

    assert isinstance(form, Form)
