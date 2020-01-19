from django.shortcuts import render
from . import forms

def index(request):
    form = forms.IndexForm()
    result = render(
        request=request,
        template_name='lostcitiesscore/index.html',
        context={'form': form})

    return result
