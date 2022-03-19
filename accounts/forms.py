from django import forms
from accounts.models import UserAccount

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