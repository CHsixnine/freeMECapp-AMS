"""
URL configuration for AMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Registrations import views
from Subscription.views import *

urlpatterns = [
    path('amsi/v1/admin/', admin.site.urls),
    path('amsi/v1/queries/adjacent_app_instances', views.adjacent_app_instances),
    path('amsi/v1/app_mobility_services', views.app_mobility_services),
    path('amsi/v1/app_mobility_services/<str:appMobilityServiceId>', views.app_mobility_services_with_id),
    path('amsi/v1/app_mobility_services/<str:appMobilityServiceId>/deregister_task', views.app_mobility_services_with_deregister),
    path('amsi/v1/subscriptions', views.subscriptions),
    path('amsi/v1/subscriptions/<str:subscriptionId>', views.subscriptions_with_id),
    path('amsi/v1/uri_provided_by_subscriber', views.uri_provided_by_subscriber),
    path('amsi/v1/evt_sink', evt_sink)
]
