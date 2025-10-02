# borrow_logs/models.py
from django.db import models
from django.conf import settings

class BorrowLog(models.Model):
    game = models.ForeignKey('boardgames.BoardGame', on_delete=models.CASCADE) # เกมที่ถูกยืม
    borrowed_by_staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # พนักงานที่ทำการยืม
    customer_name = models.CharField(max_length=255) # ชื่อของลูกค้าที่ยืม
    borrow_date = models.DateTimeField(auto_now_add=True) # วันที่ยืม
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.game.name} borrowed by {self.customer_name}" # เปลี่ยนเป็นชื่อลูกค้าจะสื่อความหมายกว่า