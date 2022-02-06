from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name = 'orders'),
    path('detail/<int:id>', views.detail, name='detail-order'),
    path('upload/', views.upload, name='upload-order'),
]