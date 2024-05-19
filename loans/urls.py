from django.urls import path
from . import views

urlpatterns = [
    path('', views.loan_list, name='loan_list'),
    path('loan/new/', views.loan_create, name='loan_create'),
    path('loan/<int:pk>/', views.loan_detail, name='loan_detail'),
    path('loan/<int:pk>/edit/', views.loan_update, name='loan_update'),
    path('loan/<int:pk>/delete/', views.loan_delete, name='loan_delete'),
]