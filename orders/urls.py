from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name = 'orders'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail-order'),
    path('upload/', views.upload, name='upload-order'),
]