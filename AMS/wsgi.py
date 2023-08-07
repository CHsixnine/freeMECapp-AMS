"""
WSGI config for AMS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from utils.ams_mqtt_client import AMS_MQTT_CLIENT
from utils.mec_app_host_info import MEC_App_Host_Info
from utils.cell_change_subscription import CellChangeSubscription
from utils.mp1_agent import Mp1_Agent
from AMS.settings import APPINSTANCE_ID
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AMS.settings')

application = get_wsgi_application()

mp1 = Mp1_Agent()
mec_app_host_info = MEC_App_Host_Info()

mp1.service_registration(appInstanceId=APPINSTANCE_ID)
rnis_url = mp1.service_availability_query(appInstanceId=APPINSTANCE_ID, serviceId="rnisergtqefhhg")["serCategory"]["href"]

cell_change_subscription=CellChangeSubscription(
    callback_url = mec_app_host_info.get_mec_app_ip()+":"+str(sys.argv[-1].split(':',1)[1])+"/amsi/v1/evt_sink",
    ams_appInstanceId = mec_app_host_info.get_hostname(),
    rnis_host = rnis_url,
)

cell_change_subscription.subscribe()


# mqtt_client = AMS_MQTT_CLIENT("10.0.0.218")
# mqtt_client.recv(topic="CaReconfNotification")