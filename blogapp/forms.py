from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUsers
import re 


class Register_form(UserCreationForm):
    password1 = forms.CharField(error_messages={'required': 'Enter password'}, label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter Password','class': 'form-control'}))
    password2 = forms.CharField(error_messages={'required': 'Enter password again'},label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter Confirm Password','class': 'form-control'}))
    email = forms.EmailField(error_messages={'required' : 'Email is required'},widget=forms.EmailInput(attrs={'placeholder':'Enter Email','class': 'form-control'}) )
    policy = forms.BooleanField(required = True , error_messages={'required' : 'Email is required'})
    class Meta:
        model = CustomUsers
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'email': 'Email',
                  }
        widgets = {'username': forms.TextInput(attrs={'placeholder':'Enter Username','class': 'form-control','onkeyup':'keyname()','onblur':'blurname()'}),
                   'first_name': forms.TextInput(attrs={'placeholder':'Enter First Name','class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'placeholder':'Enter Last Name','class': 'form-control'}),
                   }
        error_messages={
                    'username' : { 'required' : 'please enter username '},
        }           
    
    def __init__(self, *args, **kwargs):
        super(Register_form, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

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
