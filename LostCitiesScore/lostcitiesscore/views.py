from django.shortcuts import render

def index(request):
    result = render(
        request=request,
        template_name='lostcitiesscore/index.html',
        context={})

    return result
