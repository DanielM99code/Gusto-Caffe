from django import forms
from .models import Message

class FormMessage (forms.ModelForm):
    user_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'type': 'text', 'id': 'name', 'class': 'form-control',
                                                              'placeholder': 'Name', 'required': 'required'}))

    user_email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email', 'id': 'email', 'class': 'form-control',
                                                              'placeholder': 'Email', 'required': 'required'}))
    user_message = forms.CharField(max_length=400, widget=forms.Textarea(attrs={'type': 'message', 'id': 'message', 'class': 'form-control',
                                                              'placeholder': 'Message', 'required': 'required'}))

    class Meta():
        model = Message
        fields = ('user_name', 'user_email', 'user_message')