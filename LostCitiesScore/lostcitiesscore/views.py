from django.shortcuts import render
from . import forms

def index(request):
    form = forms.IndexForm(data=request.POST.dict() or None)

    if request.method == 'POST':
        if form.is_valid:
            print('YAAAAAAY')

    result = render(
        request=request,
        template_name='lostcitiesscore/index.html',
        context={'form': form})

    return result
