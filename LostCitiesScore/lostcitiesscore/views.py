from django.shortcuts import render
from . import forms

def index(request):
    form = forms.IndexForm()

    if request.method == 'POST':
        request.POST.get('cards_A_round_1')

    result = render(
        request=request,
        template_name='lostcitiesscore/index.html',
        context={'form': form})

    return result
