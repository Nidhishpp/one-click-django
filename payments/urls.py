"""
click URL Configuration
"""
from django.urls import path
from . import views

app_name = 'payments'
urlpatterns = [
    # path('', views.index, name='payments'),
    path('', views.PurchaseView.as_view(), name='payments'),
    path('config/', views.stripe_config),  # new
    path('create-checkout-session/', views.create_checkout_session), # new
    path('success/', views.SuccessView.as_view()), # new
    path('cancelled/', views.CancelledView.as_view()), # new
    path('webhook/', views.stripe_webhook), # new
]
