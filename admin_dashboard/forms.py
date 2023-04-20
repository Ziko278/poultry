from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Select, TextInput, CheckboxInput, CheckboxSelectMultiple, DateInput
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from admin_dashboard.models import *


class SiteSetupForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = SiteSetupModel
        fields = '__all__'

        widgets = {

        }


class ContactForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = ContactModel
        fields = '__all__'

        widgets = {

        }


class GalleryForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = GalleryModel
        fields = '__all__'

        widgets = {

        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:

        widgets = {
             'password': TextInput(attrs={
                 'class': 'form-control',
                 'type': 'password',
             }),
        }