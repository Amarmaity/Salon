from django.http import JsonResponse
# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Customer.models import Customer

import json
import os

def hello_world(requst):
    return JsonResponse({'message' : 'Hello from Django !'})


@csrf_exempt
def register_customer_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            password = data.get('password')

            Customer.objects.create(name=name, password=password)

            return JsonResponse({'message' : 'Customer registered successfully'})
        except Exception as e:
            return JsonResponse({'error' : str(e)}, status=400)
    return JsonResponse({'error' : 'Invalid  request'}, status=400)