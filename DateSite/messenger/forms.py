from django import forms
from .models import *

class MessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': 'сообщение'
    }))

    class Meta:
        model = Message
        fields = [
            'message',
        ]