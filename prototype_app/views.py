# from django.shortcuts import render
from django.http import HttpResponse
from prototype_app.util import test_helper_function


def test_view(request):
    """
    Go to the /test_view/ URL to trigger this view
    """
    result = test_helper_function()
    return HttpResponse(f'Hello World, check out this groovy result: {result}')
