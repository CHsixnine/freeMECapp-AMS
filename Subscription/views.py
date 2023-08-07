from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def evt_sink(request):
    payload = json.loads(request.body.decode("utf-8"))
    print(payload)
    return JsonResponse(payload, status=200)
