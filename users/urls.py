from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('', views.log_home, name="log_home"),
    path('login/', views.login, name="login"),
    path('mypage/', views.mypage, name="mypage"),
    path('<int:user_id>/mypage_update/',views.mypage_update,name="mypage_update"), 
    path('about/', views.about, name="about"),
    path('logout/', views.logout, name="logout"),
]
