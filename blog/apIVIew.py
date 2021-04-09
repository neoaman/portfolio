# Importing the required modules
from rest_framework.views import APIView,Response,status
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView
from bson import ObjectId
import json
from rest_framework.decorators import action

# importing required models and serializers
from .models import BlogPost
from .serializers import BlogPostSerializer

# Importing utility functions/class
from utility.apps import mongodb
from utility.templatetags.template_extra import md_safe


# Class and function for API view
class BlogPostView_(viewsets.ViewSet):
    """
    Blog Post with Auto generated __ID__
    """
    # action = "list"
    view_name = {
        "list":{
            "name":"Blog List",
            "description":''' this will show all __blogs__  '''},
        "retrive":{
            "name":"Blog Retrive",
            "description":''' this is the __retrive__ blogs page  '''},
        "create":{"name":"Blog Create",
            "description":''' this is the __create__ blogs page  '''},
        "update":{
            "name":"Blog Update",
            "description":''' this is the __update__ blogs page  '''},
        "partial_update":{
            "name":"Blog Update",
            "description":''' this is the __update__ blogs page  '''},
        "destroy":{
            "name":"Blog Delete",
            "description":''' this is the __destroy__ blogs page '''},
        None:{
            "name":"Blog Retrive",
            "description":''' this is the __retrive__ blogs page  '''},
        
        }

    def get_view_name(self):
        if not hasattr(self,'action'):
            return "Blog"
        else:
            print(self.action)
            return self.view_name[self.action]["name"]
            

    
    def get_view_description(self,html=True):
        if self.action:
            description = self.view_name[self.action]["description"]
            return md_safe(description)

        return ""

    

    serializer_class = BlogPostSerializer
    collection = mongodb(use="blog")
    lookup_field = "postId"
    json_fields = BlogPost.json_field

    def list(self,request,*args,**kwargs):


        context = [self.serializer_class(i,context={'request':request}).data for i in self.collection.filter({})]
        # except:
        #     context = [{"error":"No data Found"},{"info":"Add some data"}]

        return Response(context,status=status.HTTP_200_OK)

    def create(self,request,*args,**kwargs):

        data = self.serializer_class(request.data).data
        
        # latest_data = self.collection.get({},sort=[('_id',-1)])
        # if not latest_data: latest_data={}
        # data[self.lookup_field] = str(int(latest_data.get(self.lookup_field,0))+1)
        
        for i in self.json_fields : data[i] = json.loads(data[i])
        self.collection.add(value=data)

        return Response(self.serializer_class(data,context={'request':request}).data, status=status.HTTP_200_OK)
    
    def retrive(self,request,pk=None,**kwargs):

        context = self.serializer_class(self.collection.get({self.lookup_field:pk}),context={'request':request}).data

        return Response(context, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):

        # print(request.data)
        data = self.serializer_class(request.data).data
        # print(data)
        for i in self.json_fields: data[i] = json.loads(data[i])
        self.collection.set_all({self.lookup_field:pk},data)

        context = self.serializer_class(self.collection.get({self.lookup_field:pk}),context={'request':request}).data
        return Response(context, status=status.HTTP_200_OK)
        

    def partial_update(self, request, pk=None):

        data = self.serializer_class(request.data).data
        for i in self.json_fields: data[i] = json.loads(data[i])
        self.collection.set_all({self.lookup_field:pk},data)

        context = self.serializer_class(self.collection.get({self.lookup_field:pk}),context={'request':request}).data
        return Response(context, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        
        self.collection.delete({self.lookup_field:pk})
        context={"info":f"Object with ID {pk} Deleted sucessfully"}

        return Response(context, status=status.HTTP_200_OK)