"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class submitPayment(forms.Form):
    invoice_ID = forms.CharField(label = "Invoice ID", max_length=10)
    company_ID = forms.CharField(label = "Company ID", max_length=10)
    payment_ID = forms.CharField(label = "Payment ID", max_length=10)
    payment_Date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    payment_Type = forms.CharField(label = "Payment Type", max_length=300)