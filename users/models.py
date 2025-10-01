# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Django มี username, password, fullname (first_name, last_name) ให้แล้ว
    # เราจะเพิ่มแค่ 'role' เข้าไป
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')

    # --- ส่วนที่เพิ่มเข้ามาเพื่อแก้ Error ---
    # เราต้องกำหนด related_name ใหม่เพื่อไม่ให้ชนกับ User Model พื้นฐานของ Django
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="custom_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions_set",
        related_query_name="user",
    )