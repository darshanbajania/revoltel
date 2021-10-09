from django import forms
import re
# from formValidationApp.models import *
class ContactForm(forms.Form):
    name = forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class' : 'form-field'}))
    mobile = forms.IntegerField(label='Mobile number',widget=forms.TextInput(attrs={'class' : 'form-field'}))
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class' : 'form-field'}))
    co_name = forms.CharField(label='Company Name',widget=forms.TextInput(attrs={'class' : 'form-field'}))
    message = forms.CharField(label='Message',widget=forms.Textarea(attrs={'placeholder': 'Type your query here','class' : 'form-field'}))

    def clean(self):

        super(ContactForm, self).clean()
        mobile = self.cleaned_data.get('mobile')

        rule = re.compile(r'(^[+0-9]{1,3})*([0-9]{10,11}$)')
        if len(str(mobile)) < 10:
            self._errors['mobile'] = self.error_class(['Valid mobile number required'])
            print(mobile)

        return self.cleaned_data