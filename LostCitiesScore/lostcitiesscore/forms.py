from django import forms



class IndexForm(forms.Form):
    cards_A_round_1 = forms.CharField()
    cards_B_round_1 = forms.CharField()

    cards_A_round_2 = forms.CharField()
    cards_B_round_2 = forms.CharField()

    cards_A_round_3 = forms.CharField()
    cards_B_round_3 = forms.CharField()
