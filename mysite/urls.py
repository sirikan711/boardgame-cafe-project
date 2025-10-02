# mysite/urls.py
from django.contrib import admin
from django.urls import path, include 
from users.views import signup_view, login_view, logout_view
# แก้ไขการ import ให้รวม view ใหม่ๆ เข้ามาด้วย
from boardgames.views import index_view, add_game_view, edit_game_view, delete_game_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),

    path('', index_view, name='index'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('games/add/', add_game_view, name='add_game'),
    # --- เพิ่ม 2 บรรทัดนี้ ---
    path('games/<int:pk>/edit/', edit_game_view, name='edit_game'),
    path('games/<int:pk>/delete/', delete_game_view, name='delete_game'),
]