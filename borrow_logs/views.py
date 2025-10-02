# borrow_logs/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from boardgames.models import BoardGame
from .models import BorrowLog
from .forms import BorrowForm

@login_required
def borrow_game_view(request, pk):
    if request.user.role not in ['admin', 'staff']:
        return redirect('index')

    game = get_object_or_404(BoardGame, pk=pk)

    # ถ้าเกมไม่ว่าง ให้กลับไปหน้าแรกเลย
    if game.status != 'available':
        return redirect('index')

    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            borrow_log = form.save(commit=False)
            borrow_log.game = game
            borrow_log.borrowed_by_staff = request.user
            borrow_log.borrow_date = timezone.now()
            borrow_log.save()

            # อัปเดตสถานะเกมเป็น 'borrowed'
            game.status = 'borrowed'
            game.save()

            return redirect('index')
    else:
        form = BorrowForm()

    return render(request, 'borrow_game_form.html', {
        'form': form,
        'game': game
    })

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

@login_required
def report_view(request):
    # จำกัดการเข้าถึงเฉพาะ Admin เท่านั้น
    if request.user.role != 'admin':
        return redirect('index')

    # ดึงข้อมูล Log การยืมทั้งหมด โดยเรียงจากวันที่ยืมล่าสุด (descending)
    logs = BorrowLog.objects.all().order_by('-borrow_date')

    context = {
        'logs': logs
    }
    return render(request, 'report.html', context)