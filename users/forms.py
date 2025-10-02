# users/forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('fullname', 'email') # เพิ่ม field ที่ต้องการให้แสดงในฟอร์ม

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True  # <-- กำหนดให้เป็น staff ที่นี่
        user.role = 'staff'   # <-- กำหนด role ที่นี่เพื่อความแน่นอน
        if commit:
            user.save()
        return user