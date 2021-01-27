from django import forms

class NameForm(forms.Form):
    task = forms.CharField(label='Task', max_length=100)
