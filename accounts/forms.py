from django import forms
from accounts.models import Profile, UserAccount
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password'
    }))
    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'Firstname'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Lastname'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    def clean(self):
        clean_data = super(RegistrationForm, self).clean()
        password = clean_data.get('password')
        confirm_password = clean_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('Password must match')

class ProfileCreationForm(forms.ModelForm):
    bio = forms.CharField( widget = forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder': 'More about you...',
        'cols': 200,
        'rows': 3,
        'style': 'width: 100%'
    }))
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'location']

    def __init__(self, *args, **kwargs):
        super(ProfileCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields: 
            self.fields[field].widget.attrs['class'] = 'form-control'