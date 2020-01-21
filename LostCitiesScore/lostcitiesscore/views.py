from django.shortcuts import render
from . import forms

def index(request):
    form = forms.IndexForm(data=request.POST.dict() or None)
    template = 'lostcitiesscore/index.html'
    scores = None
    context = {
        'form': form,
        'scores': scores,
    }

    if form.is_valid():
        player_1_round_1 = form.data
        print(player_1_round_1)
        template = 'lostcitiesscore/scores.html'

    result = render(
        request=request,
        template_name=template,
        context=context)

    return result
