# boardgames/views.py
from django.shortcuts import render, redirect, get_object_or_404 # เพิ่ม get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BoardGame
from .forms import BoardGameForm


def index_view(request):
    # --- เพิ่ม Logic การค้นหา ---
    search_query = request.GET.get('q', None) # ดึงค่าจาก URL ที่มี name='q'

    if search_query:
        # ถ้ามีการค้นหา ให้กรองข้อมูลเกมตามชื่อ
        # __icontains คือการค้นหาแบบ "contains" และไม่สนตัวพิมพ์เล็ก/ใหญ่
        games = BoardGame.objects.filter(name__icontains=search_query)
    else:
        # ถ้าไม่มีการค้นหา ให้แสดงเกมทั้งหมดเหมือนเดิม
        games = BoardGame.objects.all() 
    
    context = {
        'games': games,
        'search_query': search_query, # ส่งค่าที่ค้นหากลับไปให้ template
    }
    
    return render(request, 'index.html', context)

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