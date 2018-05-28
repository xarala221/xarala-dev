from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import View, FormView, CreateView, DetailView

from blog.forms import JoinForm
from blog.models import JoinUs
# Create your views here.

"""
def blog(request):
    return render(request, "blog/all_post.html")
"""
class HomeView(SuccessMessageMixin, CreateView):
  template_name = "blog/all_post.html"
  form_class = JoinForm
  success_url = '/blog/'
  def get_context_data(self, *args, **kwargs):
      context = super(HomeView, self).get_context_data(*args, **kwargs)
      context['object'] = JoinUs.objects.filter().first()
      return context

  def get_success_message(self, cleaned_data):
    print(cleaned_data)
    return "Thank You For Joining!"



def details(request):
    return render(request, "blog/post_detail.html")
