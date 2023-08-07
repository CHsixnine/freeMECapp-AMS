from threading import Thread
import json
import requests

class CellChangeSubscription():
    def __init__(self, callback_url , ams_appInstanceId, rnis_host):
        self.callback_url = callback_url
        self.ams_appInstanceId = ams_appInstanceId 
        self.rnis_host = rnis_host

    def subscribe(self):
        payload = {
            "subscriptionType": "CellChangeSubscription",
            "callbackReference": self.callback_url,
            "requestTestNotification": False,
            "websockNotifConfig": {
                "description": "the subscrib rnis config",
                "websocketUri": self.callback_url,
                "requestWebsocketUri": False
            },
            "_links": {
                "description": "the subscrib rnis ID",
                "self": {
                    "href": "CellChangeNotificationFor"+self.ams_appInstanceId
                }
            },
            "filterCriteriaAssocHo": {
                "description": "",
                "appInstanceId": self.ams_appInstanceId,
                "associateId": [
                    {
                        "type": "1",
                        "value": "60.60.0.1"
                    }
                ],
                "ecgi": [
                    {
                        "cellId": "1",
                        "plmn": {
                            "mcc": "208",
                            "mnc": "93"
                        }
                    }
                ],
                "hoStatus": [
                    1
                ],
            },
            "expiryDeadline": {
                "nanoSeconds": "time",
                "Seconds": "time"
            },
        }
        rnis_subscription_url = "http://{rnis_host}/rni/v2/subscriptions".format(rnis_host=self.rnis_host)
        payload = json.dumps(payload)
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cache-Control': 'no-cache',
        }
        response = requests.request("POST", rnis_subscription_url, headers=headers, data=payload)
        return json.loads(response.text)