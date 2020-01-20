from django import forms


######################################~
from django.core.exceptions import ValidationError

def validate_school_email(value):
    if not ".edu" in value:
        raise ValidationError("A valid school email must be entered in")
    else:
        return value

######################################~



def validator(*args, **kwargs):
    print('---VALIDATOR---')
    print(args)
    print(kwargs)
    print('---VALIDATOR END---')


# ValidationError(_('Invalid value'), code='invalid')

# # Good
# ValidationError(
#     _('Invalid value: %(value)s'),
#     params={'value': '42'},
# )

    raise ValidationError("A valid school email must be entered in")
    # return False



class IndexForm(forms.Form):
    """
    For starters, a reduntant
    simple form with both player all rounds.
    """
    cards_A_round_1 = forms.CharField(validators=[validator])
    cards_B_round_1 = forms.CharField()

    cards_A_round_2 = forms.CharField()
    cards_B_round_2 = forms.CharField()

    cards_A_round_3 = forms.CharField()
    cards_B_round_3 = forms.CharField()




