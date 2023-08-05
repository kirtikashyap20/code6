from django.views.generic import TemplateView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#URLConf

urlpatterns =[
    path('',TemplateView.as_view(template_name='user_roles.html')),
    path('profile/', views.profile, name='profile'),
    path('users/', views.users, name='users'),
    path('users/detail/<str:pk>', views.detail_user, name='detail_user'),
    path('profile/roles/<str:pk>', views.get_roles, name='get_roles'),

    path('punch/', views.add_punch, name='add_punch'),
    path('gate_user/', views.gate_user, name='gate_user'),
    path('crane_user/', views.crane_user, name='crane_user'),
    path('ip/', views.get_client_ip, name='get_client_ip'),
    path('map/', views.show_map, name='show_map'),
    # path('', views.add_task, name='add_task'),
    ]