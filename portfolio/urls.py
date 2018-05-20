from django.conf.urls import url
from portfolio.views import *


urlpatterns = [
  url(r"^$", index, name="home")
]