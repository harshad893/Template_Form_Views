from django import forms
from app.models import *
class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    mobile=forms.CharField(max_length=10,min_length=10)

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'