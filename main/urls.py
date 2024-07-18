from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('info/<int:id>/', views.index_info, name='index_info'),
]