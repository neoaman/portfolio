from django.db import models
from utility.apps import mongodb

# Create your models here.
def auto_id():
    collection = mongodb(use="blog")
    return str(collection.filter({}).count()+1)

class BlogPost(models.Model):
    postId = models.CharField(max_length=10,default=auto_id,unique=True)
    title = models.CharField(max_length=100)
    subTitle = models.CharField(max_length=100)
    image = models.ImageField()
    publishDate = models.DateTimeField()
    draft = models.BooleanField()
    tag = models.JSONField()
    content = models.TextField()

    json_field = ["tag"]

    # Clean_<field_name> works on admin default db model
    def clean_tag(self):
        print(type(self.tag))
        
        return self.tag.split(",")

