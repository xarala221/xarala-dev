from django.conf.urls import url
#from portfolio.views import *
from portfolio.views import HomeView



urlpatterns = [
  url(r"^$", HomeView.as_view(), name="home")
]