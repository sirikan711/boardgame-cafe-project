# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# เราจะใช้ชื่อ Model ของเราโดยตรง ไม่ต้อง import User ดั้งเดิมมา unregister
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'fullname', 'role', 'is_staff')
    
    # fieldsets จะเป็นการกำหนดรูปแบบการแสดงผลในหน้าแก้ไข
    # เราเพิ่ม 'Custom Fields' เข้าไปต่อจากของเดิม
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('fullname', 'role')}),
    )
    # add_fieldsets ใช้สำหรับหน้าสร้าง User ใหม่ใน Admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('fullname', 'role')}),
    )

# ลงทะเบียน Model ของเราด้วย Admin class ที่เราสร้างขึ้น
admin.site.register(User, CustomUserAdmin)