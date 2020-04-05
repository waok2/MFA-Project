#from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.paydashboard, name='paydashboard'),
    path('newloan/', views.newloan, name='newloan'),
    path('newpay/', views.newpay, name='newpay'),
    path('loans/', views.loans, name='loans'),
    path('payements/', views.payments, name='payements'),
    path('loan/<int:loan_id>', views.loan, name='loan'),
]
