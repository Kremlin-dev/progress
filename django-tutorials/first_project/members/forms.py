from django import forms

class userform(forms.Form):
    username = forms.CharField(label="username", max_length =255)
    email = forms.EmailField(label="email")
    password= forms.CharField(label="password")

class signupForm(forms.Form):
    firstname= forms.CharField(label='firstname', max_length=255)
    lastname = forms.CharField(label='lastname')
    age = forms.IntegerField(label="age")