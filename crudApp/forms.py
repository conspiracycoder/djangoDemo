from random import choices
from tkinter import Label

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('super_admin', 'Super Admin'),
]

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}), max_length=30, required=True, help_text='Enter your first name.')
    last_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}), max_length=30, required=True, help_text='Enter your last name.')
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), max_length=254,required=True, help_text='Required. Inform a valid email address.')
    address = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Home Address'}),required=False, help_text='Optional.')
    city = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), max_length=30, required=False, help_text='Optional.')
    state = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}), max_length=30, required=False, help_text='Optional.')
    country = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), max_length=30, required=False, help_text='Optional.')
    zip_code = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip'}), max_length=30, required=False, help_text='Optional.')
    role = forms.ChoiceField(choices=ROLE_CHOICES, label="", widget=forms.Select(attrs={'class': 'form-control'}), required=True, help_text='Select a role.')

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'address', 'city', 'state', 'country', 'zip_code', 'role', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class UpdateRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
    country = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Country", "class": "form-control"}), label="")
    zip_code = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")
    role = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control'}), choices=ROLE_CHOICES, label="")

    class Meta:
        model = CustomUser
        exclude = ("user", "password","last_login", "is_superuser", "is_staff", "is_active", "groups", "user_permissions", "username", "date_joined", )