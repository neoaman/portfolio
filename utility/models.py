from django.db import models
# from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class MongoCredential(models.Model):
    use = models.CharField(max_length=50)
    uri = models.CharField(max_length=200)
    db = models.CharField(max_length=50)
    collection = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.use+"  "+self.collection+"  "+str(self.status)

class Bucket_Credential(models.Model):
    use = models.CharField(max_length=50)
    client_access_key = models.CharField(max_length=50)
    client_access_secret = models.CharField(max_length=50)
    bucket = models.CharField(max_length=50)
    folder = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.use+"  "+self.bucket+"  "+self.folder+"  "+str(self.status)
    
@receiver(post_save,sender=User)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)
