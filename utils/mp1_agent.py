from AMS.settings import MEP_HOST
import requests
import json
import sys
from utils.mec_app_host_info import MEC_App_Host_Info

class Mp1_Agent():
    def __init__(self):
        pass

    def service_registration(self, appInstanceId):
        self.MEP_SERVICE_REGISTRATION_URL = "http://{MEP_HOST}/mec_service_mgmt/v1/applications/{appInstanceId}/services".format(MEP_HOST=MEP_HOST, appInstanceId=appInstanceId)
        mec_app_host_info = MEC_App_Host_Info()
        payload = {
            "serInstanceId": mec_app_host_info.get_hostname(),
            "serName": "AMS",
            "serCategory": {
                "href": mec_app_host_info.get_mec_app_ip()+":"+str(sys.argv[-1].split(':',1)[1]),
                "id": "AMSergtqefhhg",
                "name": "AM",
                "version": "1.0.0"
            },
            "version": "1.0.0",
            "state": "ACTIVE",
            "transportInfo": {
                "id": "AMSergtqefhhgtransport",
                "name": "amtsransport",
                "description": "ams use restapi",
                "type": "REST_HTTP",
                "protocol": "http",
                "version": "2.0",
                "security": {
                "oAuth2Info": {
                    "grantTypes": [
                    "OAUTH2_AUTHORIZATION_CODE"
                    ],
                    "tokenEndpoint": "string"
                }
                },
                "implSpecificInfo": {}
            },
            "serializer": "JSON",
            "scopeOfLocality": "MEC-51",
            "consumedLocalOnly": True,
            "isLocal": True,
            "livenessInterval": 0,
            "_links": {
                "self": {
                "href": mec_app_host_info.get_mec_app_ip()+":"+str(sys.argv[-1].split(':',1)[1])
                },
                "liveness": {
                "href": mec_app_host_info.get_mec_app_ip()+":"+str(sys.argv[-1].split(':',1)[1])
                }
            }
            }
        payload = json.dumps(payload)
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cache-Control': 'no-cache',
        }
        response = requests.request("POST", self.MEP_SERVICE_REGISTRATION_URL, headers=headers, data=payload)
        return json.loads(response.text)

    def service_availability_query(self, appInstanceId, serviceId):
        self.MEP_SERVICE_AVAILABILITY_QUERY_URL = "http://{MEP_HOST}/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}".format(MEP_HOST=MEP_HOST, appInstanceId=appInstanceId, serviceId=serviceId)
        payload = ""
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cache-Control': 'no-cache',
        }
        response = requests.request("GET", self.MEP_SERVICE_AVAILABILITY_QUERY_URL, headers=headers, data=payload)
        return json.loads(response.text)

    def access_other_mec_app(self, URL, payload, method, headers):
        pass
