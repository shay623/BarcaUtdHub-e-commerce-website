from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone', 'address', 'city', 
                  'postal_code', 'province', 'payment_method']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name',
                'style': 'background-color: var(--bg-dark); border: 1px solid #444; color: var(--text-light); padding: 12px; border-radius: 5px; margin-bottom: 15px; width: 100%;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
                'style': 'background-color: var(--bg-dark); border: 1px solid #444; color: var(--text-light); padding: 12px; border-radius: 5px; margin-bottom: 15px; width: 100%;'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number (e.g., 0123456789)',
                'style': 'background-color: var(--bg-dark); border: 1px solid #444; color: var(--text-light); padding: 12px; border-radius: 5px; margin-bottom: 15px; width: 100%;'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Street Address',
                'style': 'background-color: var(--bg-dark); border: 1px solid #444; color: var(--text-light); padding: 12px; border-radius: 5px; margin-bottom: 15px; width: 100%;'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City',
                'style': 'background-color: var(--bg-dark); border: 1px solid #444; color: var(--text-light); padding: 12px; border-radius: 5px; margin-bottom: 15px; width: 100%;'
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Postal Code',
                'style': 'background-color: var(--bg-dark); border: 1px solid #444; color: var(--text-light); padding: 12px; border-radius: 5px; margin-bottom: 15px; width: 100%;'
            }),
            'province': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Province',
                'style': 'background-color: var(--bg-dark); border: 1px solid #444; color: var(--text-light); padding: 12px; border-radius: 5px; margin-bottom: 15px; width: 100%;'
            }),
            'payment_method': forms.Select(attrs={
                'class': 'form-control',
                'style': 'background-color: var(--bg-dark); border: 1px solid #444; color: var(--text-light); padding: 12px; border-radius: 5px; margin-bottom: 15px; width: 100%;'
            }),
        }