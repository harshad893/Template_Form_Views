from django import forms

class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    mobile=forms.CharField(max_length=10,min_length=10)