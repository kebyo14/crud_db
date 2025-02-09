from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('signup\/', views.create_item, name='create_item'),  # Регистрация
    path('signin/', views.link_item, name='link_item'),  # Вход
    path('logout/', views.logout_view, name='logout'),
    path('view_data/', views.view_data, name='view_data'),
    path('update_data/<int:user_id>/', views.update_data, name='update_data'),
    path('delete_data/<int:user_id>/', views.delete_data, name='delete_data'),

   
    path('base/', views.base, name='base'),
]
