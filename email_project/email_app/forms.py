from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
    sender_email = forms.EmailField(required=True, label='Your Email')
    sender_password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Your App Password')
    
    class Meta:
        model = Email
        fields = ['sender_email', 'sender_password', 'receiver', 'cc', 'subject', 'body', 'attachment']
