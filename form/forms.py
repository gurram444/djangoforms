from django import forms
class NameForm(forms.Form):
    First_name = forms.CharField(label='Enter First name', max_length=10)
    Last_name = forms.CharField(label='Enter Last name', max_length=10)

