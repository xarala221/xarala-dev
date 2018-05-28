from django.conf.urls import url
from blog.views import *
#from .views import HomeView


urlpatterns = [
    url(r"^$", HomeView.as_view(), name="blog"),
    url(r"^detail/$", details, name="details"),
]
