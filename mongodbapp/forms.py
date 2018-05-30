from django import forms

class ToolForm(forms.Form):
    label = forms.CharField(label='Label', max_length=100)
    description = forms.CharField(label='Description', max_length=100)