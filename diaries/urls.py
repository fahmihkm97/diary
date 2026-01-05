from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # AUTH (Login/Logout)
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # CRUD (Edit & Delete)
    path('delete/<uuid:id>/', views.delete_entry, name='delete_entry'),
    path('edit/<uuid:id>/', views.edit_entry, name='edit_entry'),
]