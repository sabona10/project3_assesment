from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/delete/<int:widget_id>/', views.delete_widget, name='delete'),
    path('/create/', views.create_widget, name='create'),
]