# authentication/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile, Punch, Role, Tasks
# class LoginForm(forms.Form):
#     username = forms.CharField(
#                     max_length=63                   
#                     )
#     password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Username'
                }
            ),
            'password' : forms.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Password'
                }
            ),
        }

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        widgets = {
            'avatar' : forms.FileInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'avatar'
                }
            ),
            'bio' : forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'bio'
                }
            ),
        }


class AddSetRole(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role']
        widgets = {
            'role' : forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Select Role'
                }
            )
        }


class AddPunch(forms.ModelForm):
    class Meta:
        model = Punch
        fields = ['user','status']
        widgets = {
            'user' : forms.Select(
                attrs={
                    'class':'form-control mb-3',
                }
            ),
            'status' : forms.Select(
                attrs={
                    'class':'form-control ',
                }
            )
        }


class Add_Task(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['user','task']
        widgets = {
            'user' : forms.Select(
                attrs={
                    'class':'form-control mb-3',
                }
            ),
            'task' : forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'bio'
                }
            )
        }