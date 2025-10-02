# users/forms.py
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'fullname')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.role = 'staff'
        if commit:
            user.save()
        return user