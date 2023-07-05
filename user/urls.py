from django.urls import path
from .views import registration_view, login_view, logout_view, profile_view, img_upload, img_delete

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('user/profile/', profile_view, name='profile'),
    path('user/img/upload/', img_upload, name='img_upload'),
    path('delete/img/<int:id>/', img_delete, name="img_delete")
]