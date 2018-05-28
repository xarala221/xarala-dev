from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
  email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control form-control-lg', 'required': 'True'}))
  name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control form-control-lg', 'required': 'True'}))
  message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Your Project', 'class': 'form-control form-control-lg', 'required': 'True'}))
  class Meta:
    model = Contact
    fields = ['name', 'email', 'message']

  def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        return email
        #print(email)
        #qs = Contact.objects.filter(email__iexact=email)
        #if qs.exists():
         #   print('exists')
            #raise forms.ValidationError("This email already exists")
        #return email