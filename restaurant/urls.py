from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.MenuItemView.as_view(), name='list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
