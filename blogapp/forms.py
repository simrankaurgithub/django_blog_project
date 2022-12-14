from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordResetForm, SetPasswordForm
from .models import *
import re
from django.forms import ModelForm


class Register_form(UserCreationForm):
    password1 = forms.CharField(error_messages={'required': 'password is required'}, label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Password', 'class': 'form-control', 'onkeyup': 'keypass1()', 'onblur': 'blurpass1()'}))
    password2 = forms.CharField(error_messages={'required': 'Confirm password is required'}, label='Confirm Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Confirm Password', 'class': 'form-control', 'onkeyup': 'keypass2()', 'onblur': 'blurpass2()'}))
    policy = forms.BooleanField(required=True, error_messages={
                                'required': 'Please agree the conditions'})

    class Meta:
        model = CustomUsers
        fields = ['username', 'first_name', 'last_name',
                  'email', 'phone_number', 'address', 'image']
        widgets = {'username': forms.TextInput(attrs={'placeholder': 'Enter Username', 'class': 'form-control', 'onkeyup': 'keyname()', 'onblur': 'blurname()', 'oninput': 'check_username()'}),
                   'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name', 'class': 'form-control', 'onkeyup': 'keyfname()', 'onblur': 'blurfname()'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'class': 'form-control', 'onkeyup': 'keylname()'}),
                   'email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control', 'onkeyup': 'keyemail()', 'onblur': 'bluremail()', 'oninput': 'check_email()'}),
                   'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
                   'address': forms.Textarea(attrs={'placeholder': 'Address', 'class': 'form-control', 'rows': 4, 'cols': 15}),
                   }
        error_messages = {
            'username': {'required': 'Username is required'},
            'first_name': {'required': 'First Name is required'},
            'email': {'required': 'Email is required'},
        }

    def __init__(self, *args, **kwargs):
        super(Register_form, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match("^[a-zA-Z0-9_.@-]+$", username):
            raise forms.ValidationError('Enter a valid username')
        return username

    def clean_first_name(self):
        fname = self.cleaned_data['first_name']
        if not re.match("^[a-zA-Z]*$", fname):
            raise forms.ValidationError('Enter a valid first name')
        return fname
    
    def clean_last_name(self):
        lname = self.cleaned_data['last_name']
        if not re.match("^[a-zA-Z]*$", lname):
            raise forms.ValidationError('Enter a valid last name')
        return lname    

    def clean_email(self):
        email = self.cleaned_data['email']
        print(email)
        if not re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+.[a-z]{2,3}$", email):
            raise forms.ValidationError('Enter a valid email address.')
        return email

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if not re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,200}$", password1):
            raise forms.ValidationError('Enter valid password')
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        if not re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,200}$", password2):
            raise forms.ValidationError('Enter valid confirm password')
        return password2

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if phone_number == '':
            pass
        elif not re.match("^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$", phone_number):
            raise forms.ValidationError('Enter a valid Phone number.')
        return phone_number


class Post_form(ModelForm):
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category",widget=forms.Select(attrs={'class': 'w-100 cat'}))
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {'title': forms.TextInput(attrs={'placeholder': 'Enter Title', 'class': 'form-control'}),
                   'category_id': forms.Select(attrs={'class': 'form-control'}),
                   }
    
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     print(title,"###########################################")
    #     if  not re.match("^[a-zA-Z]*$", title):
    #         raise forms.ValidationError('title field is required.')
        # return title


class login_form(AuthenticationForm):
    username = UsernameField(error_messages={'required': 'Enter username'}, widget=forms.TextInput(attrs={
                             'autofocus': False, 'placeholder': 'Enter username or email', 'class': 'form-control', 'onkeyup': 'keyname()', 'onblur': 'blurname()'}))
    password = forms.CharField(error_messages={'required': 'Enter password'}, strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-possword', 'placeholder': 'Enter password', 'class': 'form-control', 'onkeyup': 'keypass()', 'onblur': 'blurpass()'}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(
        attrs={'autofocus': 'email', 'class': 'form-control', 'placeholder': 'Enter Email'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password',
                                    widget=forms.PasswordInput(
                                        attrs={'autocomplete': 'new-password', 'placeholder': 'New Password', 'class': 'form-control'}),
                                    strip=False,
                                    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                   'placeholder': 'New Password Confirmation', 'class': 'form-control'}),
    )
