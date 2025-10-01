# boardgames/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BoardGame
from .forms import BoardGameForm

def index_view(request):
    # ดึงข้อมูล BoardGame ทั้งหมดจาก database
    games = BoardGame.objects.all() 
    # ส่งตัวแปร games ไปให้ template
    return render(request, 'index.html', {'games': games}) 

@login_required # ต้องล็อกอินก่อนถึงจะเข้าหน้านี้ได้
def add_game_view(request):
    # เช็คว่า user ที่เข้ามามี role เป็น 'admin' หรือไม่
    if request.user.role != 'admin':
        # ถ้าไม่ใช่แอดมิน ให้ redirect กลับไปหน้าหลัก
        return redirect('index')

    if request.method == 'POST':
        form = BoardGameForm(request.POST)
        if form.is_valid():
            form.save() # บันทึกข้อมูลลง database
            return redirect('index') # กลับไปหน้าหลัก
    else:
        form = BoardGameForm()

    return render(request, 'add_game.html', {'form': form})