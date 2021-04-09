from django.contrib import admin
from .models import MongoCredential,Bucket_Credential

# Register your models here.
admin.site.register(MongoCredential)
admin.site.register(Bucket_Credential)