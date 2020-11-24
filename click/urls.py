"""
click URL Configuration
"""
from django.urls import path
from . import views

app_name = 'click'
urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('services/', views.services, name='services'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('login/', views.loginView, name='login'),
    path('contact/', views.contact, name='contact'),
    path('auth/login/', views.authLogin, name='auth-login'),
    path('auth/signup/', views.authSignup, name='auth-signup'),
    path('auth/logout/', views.authLogout, name='auth-logout'),
    path('user/', views.user, name='user'),
    path('user/dashboard', views.userDashboard, name='user-dashboard'),
    path('user/bookings', views.userBooking, name='user-bookings'),
    path('user/profile', views.userProfile, name='user-profile'),
    path('user/reviews', views.userReviews, name='user-reviews'),
]
