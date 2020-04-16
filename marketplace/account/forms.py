from django import forms
from django.core.validators import MinValueValidator

class addressForm(forms.Form):
    fullname = forms.CharField()
    country = forms.CharField()
    street1 = forms.CharField()
    street2 = forms.CharField()
    city = forms.CharField()
    province = forms.CharField()
    postal_code = forms.IntegerField(validators=[MinValueValidator(0)])
    phone_num = forms.IntegerField(validators=[MinValueValidator(0)])
