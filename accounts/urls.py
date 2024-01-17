from django.urls import path, include
from .views import login_view, register_view, home_view, logout_view

urlpatterns = [
    path('', login_view, name="login"),
    #path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('home/', home_view, name="home"),
    path('logout/', logout_view, name="logout"),
]