from django import forms 
from .models import Job, Company 
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	class Meta:
		model = User 
		fields = ['username', 'email', 'password']


class JobForm(forms.ModelForm):
	class Meta:
		model = Job 
		fields = ['name', 'company']

class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ['name']