from django.urls import path
from . import views
from .views import OrderAddView

urlpatterns = [
    path('', views.orders, name = 'orders'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail-order'),
    path('upload/', OrderAddView.as_view(), name='order-upload')
]