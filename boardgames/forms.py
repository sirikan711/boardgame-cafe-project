# boardgames/forms.py
from django import forms
from .models import BoardGame

class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        # ระบุ field ทั้งหมดที่ต้องการให้แสดงในฟอร์ม
        fields = ['name', 'category', 'players_min', 'players_max', 'status']