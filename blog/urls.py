from django.urls import path,include
from .apIVIew import BlogPostView_
from .views import home,add,update
from .apiView import BlogIndividualPostView,BlogPostView

# from rest_framework.routers import DefaultRouter,SimpleRouter
# router = DefaultRouter()
# router.register("curd",BPVb,basename="api")
# router.register("curd",BlogIndividualPostView,basename="Iapi")

app_name = "blog"
urlpatterns = [
    path("",home,name="home"),
    path("add/",add,name="add"),
    path("update/<str:postId>",update,name="update"),

    # APIView
    path("api/",BlogPostView.as_view(),name="view"),
    path("api/<str:pk>/",BlogIndividualPostView.as_view(),name="individual"),

    # View.Viewset
    path("aPi/",BlogPostView_.as_view({'get':'list','post':'create'}),name="_view"),
    path("aPi/<str:pk>/",BlogPostView_.as_view({'get':'retrive','put':'update','patch':'partial_update','delete':'destroy'}),name="_individual"),

    # path("api2/",include(router.urls)), # If want to perform everything at once
]