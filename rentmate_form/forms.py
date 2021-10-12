from django import forms
from .models import profile,apartment
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password',)


class Profile(forms.ModelForm):

    class Meta:
        model = profile
        fields = {"name", "age", "mob", "user"}


class Apartment(forms.ModelForm):

    class Meta:
        model = apartment
        fields = {"locality", "address", "idproof", "housemimage", "space", "description", "email", "price"}
