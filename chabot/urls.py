from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='base'),
    path('booktrip/create/', views.booktrip_create, name='booktrip_create'),
    path('booktrip/update/<int:pk>/', views.booktrip_update, name='booktrip_update'),
    path('booktrip/cancel/', views.booktrip_cancel, name='booktrip_cancel'),
]
