from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CancerPredictionForm(forms.Form):
    mean_radius = forms.FloatField(label='Mean Radius')
    mean_texture = forms.FloatField(label='Mean Texture')
    mean_perimeter = forms.FloatField(label='Mean Perimeter')
    mean_area = forms.FloatField(label='Mean Area')
    mean_smoothness = forms.FloatField(label='Mean Smoothness')



