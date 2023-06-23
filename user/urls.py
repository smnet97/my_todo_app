from django.urls import path
from .views import registration_view, login_view, logout_view

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration')
]