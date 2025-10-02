# borrow_logs/forms.py
from django import forms
from .models import BorrowLog

class BorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowLog
        fields = ['customer_name']
        labels = {
            'customer_name': 'Customer Name'
        }