from django.shortcuts import render
from . import forms

def index(request):
    form = forms.IndexForm()

    if request.method == 'POST':
        cards_A1 = request.POST.get('cards_A_round_1')
        cards_B1 = request.POST.get('cards_B_round_1')

        cards_A2 = request.POST.get('cards_A_round_2')
        cards_B2 = request.POST.get('cards_B_round_2')

        cards_A3 = request.POST.get('cards_A_round_3')
        cards_B3 = request.POST.get('cards_B_round_3')

    result = render(
        request=request,
        template_name='lostcitiesscore/index.html',
        context={'form': form})

    return result
