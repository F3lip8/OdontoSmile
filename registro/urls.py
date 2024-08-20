from django.urls import path
from registro import views


urlpatterns = [
    path('', views.index, name='index'),
    path('calendario/', views.CalendarioView, name='calendario'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro')
]
