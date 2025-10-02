# boardgames/views.py
from django.shortcuts import render, redirect, get_object_or_404 # เพิ่ม get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BoardGame
from .forms import BoardGameForm

def index_view(request):
    games = BoardGame.objects.all() 
    return render(request, 'index.html', {'games': games}) 

@login_required
def add_game_view(request):
    if request.user.role != 'admin':
        return redirect('index')

    if request.method == 'POST':
        form = BoardGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BoardGameForm()

    return render(request, 'add_game.html', {'form': form})

# --- เพิ่มฟังก์ชันนี้เข้าไป ---
@login_required
def edit_game_view(request, pk):
    game = get_object_or_404(BoardGame, pk=pk) # ดึงข้อมูลเกมที่ต้องการแก้ไข, ถ้าไม่เจอก็ 404
    
    if request.user.role != 'admin':
        return redirect('index')

    if request.method == 'POST':
        form = BoardGameForm(request.POST, instance=game) # ส่ง instance=game เพื่อบอกว่าเป็นการแก้ไข
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BoardGameForm(instance=game) # แสดงฟอร์มพร้อมข้อมูลเดิมของเกม
        
    return render(request, 'edit_game.html', {'form': form, 'game': game})

# --- เพิ่มฟังก์ชันนี้เข้าไป ---
@login_required
def delete_game_view(request, pk):
    game = get_object_or_404(BoardGame, pk=pk)

    if request.user.role != 'admin':
        return redirect('index')

    if request.method == 'POST': # ถ้ามีการกดปุ่มยืนยันลบ
        game.delete()
        return redirect('index')

    # ถ้าเป็น GET request ให้ไปหน้ายืนยันการลบ
    return render(request, 'delete_game_confirm.html', {'game': game})