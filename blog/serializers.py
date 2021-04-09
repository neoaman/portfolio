from rest_framework import serializers
from rest_framework.views import Response,Request
from rest_framework.reverse import reverse
from .models import BlogPost
import json


from utility.apps import mongodb

def auto_id():
    lookup_field = "postId"
    collection = mongodb("blog")
    latest_data = collection.get({},sort=[('_id',-1)])
    if not latest_data: latest_data={}
    id_ = str(int(latest_data.get(lookup_field,0))+1)
    return id_

class BlogPostSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    content = serializers.CharField(
        max_length=1000,
        style={'base_template': 'textarea.html', 'rows': 30})
    
    class Meta:
        model = BlogPost
        fields = ("postId","title","tag","subTitle","content","publishDate","draft","url")

        extra_kwargs = {'draft': {'default': False},
        'postId':{'initial':auto_id},
        }
    
    def get_url(self,obj):
        # print(obj.get("postId")); print(self.context['request'])
        try: url = reverse("blog:individual",kwargs={'pk': obj.get("postId")},request=self.context.get('request',None))
        except: print("something wrong "); url = ""
        return url

    def validate_title(self, data):
        
        return data.upper()

"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
"""