from django.shortcuts import render
from django.http import JsonResponse
from product.models import Product
import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from product.serializers import ProductSerializer

# Create your views here.
@api_view(["GET","POST"])
def api_home(request, *args,**kwargs):
    """DRF api view"""
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
      data = ProductSerializer(instance).data
        
    return Response(data)
    
