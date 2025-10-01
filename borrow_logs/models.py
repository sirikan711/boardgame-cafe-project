# borrow_logs/models.py
from django.db import models
from django.conf import settings # ใช้สำหรับอ้างอิง User model

class BorrowLog(models.Model):
    game = models.ForeignKey('boardgames.BoardGame', on_delete=models.CASCADE)
    borrowed_by_staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True) # จะเป็นค่าว่างตอนที่ยังไม่คืน

    def __str__(self):
        return f"{self.game.name} borrowed by {self.borrowed_by_staff.username}"