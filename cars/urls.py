from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:car_id>/', views.detail, name='detail'),
    path('note/<int:car_id>/', views.note, name='note')
]
