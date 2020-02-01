import requests
from lostcitiesscore import views
from django.http import HttpRequest
from django.http import QueryDict


def test_alkwsjhf():
    data = QueryDict('a=1&a=2&c=3')
    request = HttpRequest()
    request.method = 'POST'


    print(dir(request))






def test_req():
    response = requests.get('http://localhost:8000')
