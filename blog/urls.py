from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('track-view/<int:pk>/', views.track_view, name='track_view'),  # 👈 This is the new one
]