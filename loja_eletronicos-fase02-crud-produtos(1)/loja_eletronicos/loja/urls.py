from django.urls import path
from . import views

app_name = 'loja'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/editar/', views.profile_edit, name='profile_edit'),
]