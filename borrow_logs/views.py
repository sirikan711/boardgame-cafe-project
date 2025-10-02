# borrow_logs/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from boardgames.models import BoardGame
from .models import BorrowLog

@login_required
def borrow_game_view(request, pk):
    # อนุญาตเฉพาะ staff และ admin
    if request.user.role not in ['admin', 'staff']:
        return redirect('index')

    game = get_object_or_404(BoardGame, pk=pk)

    # ตรวจสอบว่าเกมว่างจริงหรือไม่
    if game.status == 'available':
        # สร้าง log การยืมใหม่
        BorrowLog.objects.create(
            game=game,
            borrowed_by_staff=request.user
        )
        # อัปเดตสถานะเกมเป็น 'borrowed'
        game.status = 'borrowed'
        game.save()

    return redirect('index')

@login_required
def return_game_view(request, pk):
    # อนุญาตเฉพาะ staff และ admin
    if request.user.role not in ['admin', 'staff']:
        return redirect('index')
    
    game = get_object_or_404(BoardGame, pk=pk)

    # ตรวจสอบว่าเกมถูกยืมอยู่จริงหรือไม่
    if game.status == 'borrowed':
        try:
            # ค้นหา log การยืมล่าสุดที่ยังไม่คืนของเกมนี้
            log = BorrowLog.objects.filter(game=game, return_date__isnull=True).latest('borrow_date')
            log.return_date = timezone.now() # ใส่วันที่คืนปัจจุบัน
            log.save()
            
            # อัปเดตสถานะเกมกลับเป็น 'available'
            game.status = 'available'
            game.save()
        except BorrowLog.DoesNotExist:
            # กรณีหา log ไม่เจอ (อาจเกิดจากข้อมูลผิดพลาด)
            # บังคับให้เกมกลับมา available เพื่อแก้ปัญหาเฉพาะหน้า
            game.status = 'available'
            game.save()

    return redirect('index')