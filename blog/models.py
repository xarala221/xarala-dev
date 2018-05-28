from django.db import models

# Create your models here.
class JoinUs(models.Model):
  email = models.CharField(max_length=200)
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.email