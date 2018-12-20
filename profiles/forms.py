from django import forms

from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your first name'})
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your last name'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'location', 'gender', 'birthdate', 'bio')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your phone number'})
        self.fields['location'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your location'})
        self.fields['gender'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Choose gender'})
        self.fields['birthdate'].widget.attrs.update({
            'class': 'form-control'})
        self.fields['bio'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Tell us something about you'})


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)

    def __init__(self, *args, **kwargs):
        super(AvatarForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({
            'class': 'form-control-file',
            'accept': 'image/*'})
        self.fields['avatar'].label = ''