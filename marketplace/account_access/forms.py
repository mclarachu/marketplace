from django import forms
from django.core.exceptions import ValidationError

#checks if the password has a number in it
def validate_password_number(value):
    if not any(char.isdigit() for char in value):
        raise ValidationError(
            'Password must contain at least one number',
            code = 'no_number'
        )

def validate_password_alpha(value):
    if not any(char.isalpha() for char in value):
        raise ValidationError(
            'Password must contain at least one alphabet',
            code = 'no_alpha'
        )

class SignupForm(forms.Form):
    username = forms.CharField(
        error_messages={'required': 'You must enter a username.'}
    )

    email = forms.EmailField()
    password = forms.CharField(
        validators=[validate_password_number,validate_password_alpha],
        min_length=8,
        help_text='8 characters minimum')
    password_confirm = forms.CharField()

    def clean(self):
        cleaned_data = super(SignupForm,self).clean()

        #Validation involving multiple fields
        if 'password' in cleaned_data and 'password_confirm' in cleaned_data and cleaned_data['password'] != cleaned_data['password_confirm']:
            self.add_error('password_confirm','Passwords do not match.')
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


