from django import forms



class IndexForm(forms.Form):
    cards_A = forms.CharField()
    cards_B = forms.CharField()
