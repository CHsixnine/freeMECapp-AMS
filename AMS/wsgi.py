"""
WSGI config for AMS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from utils.ams_mqtt_client import AMS_MQTT_CLIENT
from utils.mp1_agent import Mp1_Agent
from AMS.settings import APPINSTANCE_ID

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AMS.settings')

application = get_wsgi_application()

mp1 = Mp1_Agent()
mp1.service_registration(appInstanceId=APPINSTANCE_ID)

rnis_url = mp1.service_availability_query(appInstanceId=APPINSTANCE_ID)["serCategory"]["href"]
print(rnis_url)


mqtt_client = AMS_MQTT_CLIENT("10.0.0.218")
mqtt_client.recv(topic="CaReconfNotification")