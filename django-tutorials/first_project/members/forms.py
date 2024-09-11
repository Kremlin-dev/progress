from django import forms

class userform(forms.Form):
    username = forms.CharField(label="username", max_length =255)
    email = forms.EmailField(label="email")
    password= forms.CharField(label="password")