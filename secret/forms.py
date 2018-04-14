from django import forms 
from secret.models import Post 


from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    #loginform,
    
    ) 
User = get_user_model()

class UserLoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
    	password = self.cleaned_data_get("password")

    	if not user:
    		raise forms.ValidationError
    def loginform(self):
        pass

