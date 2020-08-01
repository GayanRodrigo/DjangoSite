from django.urls import path
from .import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:deal_id>', views.detail, name='detail'),
	path('register/', views.register, name='register'),
	path('contact/', views.contact, name='contact'),
]
