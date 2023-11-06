from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

def api_view(request, *args, **kwargs):
    data = {
        'name': 'David',
        'language': 'Python'
    }
    print(request.body)
    data = json.loads(request.body)
    print(data)
    return JsonResponse(data)