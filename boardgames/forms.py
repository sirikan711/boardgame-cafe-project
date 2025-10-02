# boardgames/forms.py
from django import forms
from .models import BoardGame

class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['name', 'category', 'players_min', 'players_max', 'status']

        # กำหนด widget และ attribute ของแต่ละ field ที่นี่
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'shadow-sm appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'e.g., Catan, Splendor'
            }),
            'category': forms.TextInput(attrs={
                'class': 'shadow-sm appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'e.g., Strategy, Party'
            }),
            'players_min': forms.NumberInput(attrs={
                'class': 'shadow-sm appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'players_max': forms.NumberInput(attrs={
                'class': 'shadow-sm appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'status': forms.Select(attrs={
                'class': 'shadow-sm appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
        }