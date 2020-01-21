from django.shortcuts import render
from . import forms
from . import scorecounter as scnt

def index(request):
    form = forms.IndexForm(data=request.POST.dict() or None)
    template = 'lostcitiesscore/index.html'
    scores = None
    context = {
        'form': form,
        'scores': scores,
    }

    if form.is_valid():
        template = 'lostcitiesscore/scores.html'
        context['scores'] = [
            form.data['cards_A_round_1'],
            form.data['cards_B_round_1'],
            form.data['cards_A_round_2'],
            form.data['cards_B_round_2'],
            form.data['cards_A_round_3'],
            form.data['cards_B_round_3'],
        ]

        # pl1_r1 = form.data['cards_A_round_1']
        # pl2_r1 = form.data['cards_B_round_1']
        # pl1_r2 = form.data['cards_A_round_2']
        # pl2_r2 = form.data['cards_B_round_2']
        # pl1_r3 = form.data['cards_A_round_3']
        # pl2_r3 = form.data['cards_B_round_3']

    result = render(
        request=request,
        template_name=template,
        context=context)

    return result
