from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def hello(request, *args,**kwargs):
    body = request.body
    data = {}
    
    try:
        data = json.loads(body)
    except:
        return JsonResponse({"Message":"Data recieved failed"})
    
    print(data)
    data['headers'] = request.headers
    
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse({"Message":"Data recieved"})
    
