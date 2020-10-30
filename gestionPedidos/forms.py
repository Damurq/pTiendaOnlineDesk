from django import forms

class FormContact(forms.Form):
    subject=forms.CharField()
    mail=forms.EmailField()
    message=forms.CharField()