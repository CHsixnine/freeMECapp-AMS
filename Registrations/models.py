from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MecApp(AbstractUser):
    role = models.CharField(max_length=20, default='unverified')
    def __str__(self):
        data = dict()
        data = {
            'role':self.role,
        }
        return str(data)

class AppInfo(models.Model):
    appName = models.CharField(max_length=64, default='unverified')
    appProvider = models.CharField(max_length=64, default='unverified')
    appCategory = models.CharField(max_length=64, default='unverified')
    appDId = models.CharField(max_length=64, default='unverified')
    appInstanceId = models.CharField(max_length=64, default='unverified')
    endpoint = models.CharField(max_length=64, default='unverified')
    appServiceRequired = models.CharField(max_length=64, default='unverified')
    appServiceOptional = models.CharField(max_length=64, default='unverified')
    appFeatureRequired = models.CharField(max_length=64, default='unverified')
    appFeatureOptional = models.CharField(max_length=64, default='unverified')
    isInsByMec = models.CharField(max_length=64, default='unverified')
    appProfile = models.CharField(max_length=64, default='unverified')

    def __str__(self):
        data = dict()
        data = {
            'appName':self.appName,
            'appProvider':self.appProvider,
            'appCategory':self.appCategory,
            'appDId':self.appDId,
            'appInstanceId':self.appInstanceId,
            'endpoint':self.endpoint,
            'appServiceRequired':self.appServiceRequired,
            'appServiceOptional':self.appServiceOptional,
            'appFeatureRequired':self.appFeatureRequired,
            'appFeatureOptional':self.appFeatureOptional,
            'isInsByMec':self.isInsByMec,
            'appProfile':self.appProfile,
        }
        return str(data)

class app_mobility_services_models(models.Model):
    appMobilityServiceId = models.CharField(max_length=64, default='unverified')
    def __str__(self):
        data = dict()
        data = {
            'appMobilityServiceId': self.appMobilityServiceId
        }
        return str(data)

class subscription_models(models.Model):
    subscriptionId = models.CharField(max_length=64, default='unverified')
    def __str__(self):
        data = dict()
        data = {
            'subscriptionId': self.subscriptionId
        }
        return str(data)