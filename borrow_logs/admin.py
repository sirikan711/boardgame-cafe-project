# borrow_logs/admin.py
from django.contrib import admin
from .models import BorrowLog

# สร้าง class เพื่อปรับแต่งการแสดงผลในหน้า Admin
class BorrowLogAdmin(admin.ModelAdmin):
    list_display = ('game', 'borrowed_by_staff', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('game__name', 'borrowed_by_staff__username')

admin.site.register(BorrowLog, BorrowLogAdmin)