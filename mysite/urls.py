# mysite/urls.py
from django.contrib import admin
from django.urls import path, include
from users.views import signup_view, login_view, logout_view
from boardgames.views import index_view, add_game_view, edit_game_view, delete_game_view
from borrow_logs.views import borrow_game_view, return_game_view, report_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),

    path('', index_view, name='index'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('games/add/', add_game_view, name='add_game'),
    path('games/<int:pk>/edit/', edit_game_view, name='edit_game'),
    path('games/<int:pk>/delete/', delete_game_view, name='delete_game'),

    # --- เพิ่ม 2 บรรทัดนี้สำหรับระบบยืม-คืน ---
    path('games/<int:pk>/borrow/', borrow_game_view, name='borrow_game'),
    path('games/<int:pk>/return/', return_game_view, name='return_game'),

    # --- เพิ่มบรรทัดนี้สำหรับรายงาน ---
    path('reports/', report_view, name='report'),
]