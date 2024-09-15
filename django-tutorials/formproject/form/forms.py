from django import forms


class userRegistration(forms.Form):
    firstName = forms.CharField(label="firstName", max_length=255)
    lastName = forms.CharField(label="lastName", max_length = 255)
    email = forms.EmailField(label="email", max_length=255)
    telephone = forms.CharField(label="telephone", max_length=10)
