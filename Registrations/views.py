from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *


# Create your views here.
@csrf_exempt
def adjacent_app_instances(request):
    if request.method == 'GET':
            filter = request.GET['filter']
            all_fields = request.GET["all_fields"]
            fields = request.GET["fields"]
            exclud_fields = request.GET["exclud_fields"]
            exclud_default = request.GET["exclud_default"]

            result = [{
                "appDId": "string",
                "appInstanceCommLink": [{
                    "ipAddresses": [{
                        "host": "string",
                        "port": 0
                    }]
                }],
                "appInstanceId": "string",
                "mecHostInformation":{
                    "hostName": "string",
                    "hostId": {
                        "additionalProp1": {},
                        "additionalProp2": {},
                        "additionalProp3": {}
                    }
                },
                "registeredInstanceId": "string"
            }]
    return JsonResponse(result, status=200, safe=False)

@csrf_exempt
def app_mobility_services(request):
    if request.method == 'GET':
        filter = request.GET['filter']
        all_fields = request.GET["all_fields"]
        fields = request.GET["fields"]
        exclud_fields = request.GET["exclud_fields"]
        exclud_default = request.GET["exclud_default"]
        
        return JsonResponse("Contains a representation of the application mobility service.", status=200, safe=False)

    if request.method == 'POST':
        result = {
            "appMobilityServiceId": "string",
            "deviceInformation": [{
                "associateId": {
                    "type": "UE_IPv4_ADDRESS",
                    "value": "string"
                },
                "appMobilityServiceLevel": "APP_MOBILITY_NOT_ALLOWED",
                "contextTransferState": "NOT_TRANSFERRED"
            }],
            "expiryTime": 0,
            "serviceConsumerId": {
                "appInstanceId": "string",
                "mepId": "string"
            }
        }
        return JsonResponse(result, status=201)

@csrf_exempt
def app_mobility_services_with_id(request, appMobilityServiceId):
    if request.method == 'GET':
        result = "Contains a representation of the application mobility service."
        status = 200
    elif request.method == 'PUT':
        if not app_mobility_services_models.objects.filter(appMobilityServiceId=appMobilityServiceId):
            app_mobility_services_models.objects.create(appMobilityServiceId=appMobilityServiceId)
        result = "Contains a data type describing the updated application mobility service."
        status = 200
    elif request.method == 'DELETE':
        data = app_mobility_services_models.objects.filter(appMobilityServiceId=appMobilityServiceId)
        if data:
            data.delete()
        result = "No Content"
        status = 204
    return JsonResponse(result, status=status, safe=False)

@csrf_exempt
def app_mobility_services_with_deregister(request, appMobilityServiceId):
    if request.method == 'POST':
        if not app_mobility_services_models.objects.filter(appMobilityServiceId=appMobilityServiceId):
            app_mobility_services_models.objects.create(appMobilityServiceId=appMobilityServiceId)
        return JsonResponse("No Content", status=204, safe=False)

@csrf_exempt
def subscriptions(request):
    if request.method == 'GET':
        subscriptionType = request.GET['subscriptionType']

        result = "Contains the list of links to requestor subscriptions."
        status = 200
    elif request.method == 'POST':
        result = "Created subscription is described using the appropriate data type"
        status = 201
    return JsonResponse(result, status=status, safe=False)

@csrf_exempt
def subscriptions_with_id(request, subscriptionId):
    if request.method == 'GET':
        result = "A response body containing data type describing the specific RNI event subscription"
        status = 200
    elif request.method == 'PUT':
        if not subscription_models.objects.filter(subscriptionId=subscriptionId):
            subscription_models.objects.create(subscriptionId=subscriptionId)

        result = "a response body containing data type describing the updated subscription"
        status = 200
    elif request.method == 'DELETE':
        data = subscription_models.objects.filter(subscriptionId=subscriptionId)
        if data:
            data.delete()

        result = "No Content"
        status = 204
    return JsonResponse(result, status=status, safe=False)

@csrf_exempt
def uri_provided_by_subscriber(request):
    if request.method == 'POST':
        return JsonResponse("The notification was delivered successfully. The response body shall be empty.", status=204, safe=False)

