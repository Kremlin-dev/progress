from django import forms


class userRegistration(forms.Form):
    firstName = forms.CharField(label="firstName", max_length=25)
    lastName = forms.CharField(label="lastName", max_length = 25)
    email = forms.EmailField(label="email", max_length=255, help_text="Please use the correct email fornat")
    telephone = forms.CharField(label="telephone", max_length=10, help_text="Please use the correct telephone fornat")
