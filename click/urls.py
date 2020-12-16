"""
click URL Configuration
"""
from django.urls import path
from . import views

app_name = 'click'
urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('services/<int:id>', views.services_page, name='services'),
    path('service/<int:id>', views.service_page, name='service'),
    path('book-service/<int:id>', views.book_service, name='book-service'),
    path('book_service_insert/<int:id>', views.book_service_insert, name='book_service_insert'),
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
    path('staff/', views.staff, name='staff'),
    path('staff/dashboard', views.staffDashboard, name='staff-dashboard'),
    path('staff/bookings', views.staffBooking, name='staff-bookings'),
    path('staff/profile', views.staffProfile, name='staff-profile'),
    path('dpupdate', views.update_dp, name='dpupdate'),
    path('cancel-booking', views.cancel_booking, name='cancel_booking'),
    path('status-update', views.booking_status, name='booking_status'),
    path('booking-comment', views.booking_comment, name='booking_comment'),
    
]
