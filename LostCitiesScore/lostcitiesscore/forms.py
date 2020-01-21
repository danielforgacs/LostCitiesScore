from django import forms
from django.core.exceptions import ValidationError
from . import scorecounter


######################################~

# def validate_school_email(value):
#     if not ".edu" in value:
#         raise ValidationError("A valid school email must be entered in")
#     else:
#         return value

######################################~



def validator(value):
    # print('---VALIDATOR---')
    # # print(args)
    # # print(kwargs)
    # print(value)
    # print(value)
    # print(value)
    # print('---VALIDATOR END---')

    if not scorecounter.is_valid_score(txt=value):
        raise ValidationError("careful with the scores...")

    return value

# ValidationError(_('Invalid value'), code='invalid')

# # Good
# ValidationError(
#     _('Invalid value: %(value)s'),
#     params={'value': '42'},
# )

    # return False



class IndexForm(forms.Form):
    """
    For starters, a reduntant
    simple form with both player all rounds.
    """
    cards_A_round_1 = forms.CharField(validators=[validator])
    cards_B_round_1 = forms.CharField(validators=[validator])

    cards_A_round_2 = forms.CharField(validators=[validator])
    cards_B_round_2 = forms.CharField(validators=[validator])

    cards_A_round_3 = forms.CharField(validators=[validator])
    cards_B_round_3 = forms.CharField(validators=[validator])




