from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegisteForm(UserCreationForm):
	first_name=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
	last_name=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
	email=forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))

	class Meta:
		model=User
		fields=('username','first_name','last_name','email','password1','password2')
	def __init__(self, *args, **kwargs):
		super(RegisteForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'})
		self.fields['username'].label=''
		self.fields['username'].help_text=''
		self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Password'})
		self.fields['password1'].label=''
		self.fields['password1'].help_text=''
		self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Re-Password'})
		self.fields['password2'].label=''
		self.fields['password2'].help_text=''

class Edit_RegisteForm(UserChangeForm):
	first_name=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
	last_name=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
	email=forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
	password=forms.CharField(label='', widget=forms.TextInput(attrs={'type':'hidden'}))

	class Meta:
		model=User
		fields=('username','first_name','last_name','email','password')
	def __init__(self, *args, **kwargs):
		super(Edit_RegisteForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'})
		self.fields['username'].label=''
		self.fields['username'].help_text=''
	