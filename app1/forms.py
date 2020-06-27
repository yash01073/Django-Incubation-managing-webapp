from django import forms

class Login(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)

class Signup(forms.Form):
    firstname = forms.CharField(max_length=40)
    lastname = forms.CharField(max_length=40)
    username = forms.CharField(max_length=40)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=40,widget=forms.PasswordInput)
    mobileno = forms.CharField(max_length=10)