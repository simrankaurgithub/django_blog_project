from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re 


class Register_form(UserCreationForm):
    password1 = forms.CharField(error_messages={'required': 'Enter password'}, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(error_messages={'required': 'Enter password again'},label='Password(again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'email': 'Email',
                  }
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control','onkeyup':'keyname()','onblur':'blurname()'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control','onkeyup':'keyemail()','onblur':'bluremail()'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   }
        # error_messages={
        #             'username' : { 'required' : 'please enter username '},
        # }           
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     # valname=self.cleaned_data['username']
    #     valemail=self.cleaned_data['email']
    #     print(valemail)
    #     # if valname =="simran":
    #     #     raise forms.ValidationError('Invalid username')
    #     # if not re.match("^[a-zA-Z0-9_.+@-]+$", valname):
    #     #     raise forms.ValidationError('Invalid username')
    #     # valemail=self.cleaned_data['email']
    #     if re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$", valemail):
    #      print ("valid")  
    #     else :
    #         raise forms.ValidationError('not valid email')
