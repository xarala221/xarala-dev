from django import forms
from blog.models import JoinUs

class JoinForm(forms.ModelForm):
  email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control form-control-lg', 'required': 'True'}))
  class Meta:
    model = JoinUs
    fields = ['email',]

  def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        return email
        #print(email)
        #qs = Contact.objects.filter(email__iexact=email)
        #if qs.exists():
         #   print('exists')
            #raise forms.ValidationError("This email already exists")
        #return email