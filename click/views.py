from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.db.models import Count
from django.contrib import messages
import stripe

# Test Functions


def not_auth(user):
    return not user.is_authenticated


def is_staff(user):
    return user.is_staff


# Create your views here.
def index(request):
    categories = category.objects.filter(
        featured=1).annotate(service_count=Count('service'))
    services = service.objects.filter(featured=1)
    return render(request, 'index.html', {'categories': categories, 'services': services})


def categories(request):
    categories = category.objects.annotate(service_count=Count('service'))
    return render(request, 'categories.html', {'categories': categories})


def services_page(request, id):
    services = service.objects.filter(category=id)
    services_count = len(services)
    return render(request, 'services.html', {'services': services, 'services_count': services_count})


def service_page(request, id):
    serviceData = service.objects.annotate(
        avg_rating=Avg('comments__rating')).get(id=id)
    reviews = comments.objects.filter(service=serviceData.id)
    relateds = service.objects.filter(
        category=serviceData.category.id).exclude(id=serviceData.id)
    return render(request, 'service.html', {'service': serviceData, 'reviews': reviews, 'relateds': relateds})


def book_service(request, id):
    if request.user.is_anonymous:
        return redirect('click:login')
    service_ = service.objects.get(id=id)
    return render(request, 'book-service.html', {'service': service_})


def book_service_insert(request, id):
    serviceData = service.objects.get(id=id)
    post = booking()
    post.date = request.POST.get('date')
    post.time = request.POST.get('time')
    post.location = request.POST.get('location')
    post.phn = request.POST.get('phone')
    post.service = serviceData
    post.user = request.user
    post.save()
    # messages.success(request, 'Booking Success')

    domain_url = 'http://localhost:8000/payment/'
    stripe.api_key = settings.STRIPE_SECRET_KEY
    try:
        checkout_session = stripe.checkout.Session.create(
            # new
            client_reference_id=request.user.id if request.user.is_authenticated else None,
            success_url=domain_url + \
            'success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + 'cancelled/',
            payment_method_types=['card'],
            mode='payment',
            line_items=[
                {
                    'name': serviceData.title,
                    'quantity': 1,
                    'currency': 'inr',
                    'amount': str(serviceData.price) +'00',
                }
            ]
        )
        post.payment_id = checkout_session['payment_intent']
        post.save()
        request.session['checkout_session'] = checkout_session['id']
        # return JsonResponse({'sessionId': checkout_session['id']})
        return redirect('payments:payments')
    except Exception as e:
        print(str(e))
        # return JsonResponse({'error': str(e)})
        return redirect('/payment/cancelled/')


def cancel_booking(request):
    book = booking.objects.get(id=request.POST.get('booking_id'))
    book.reason = request.POST.get('reason')
    book.status = 'Canceled'
    book.save()
    messages.warning(request, 'Booking Canceled')
    if request.user.is_staff:
        return redirect('click:staff-bookings')
    else:
        return redirect('click:user-bookings')


def booking_status(request):
    book = booking.objects.get(id=request.POST.get('booking_id'))
    book.status = request.POST.get('status')
    book.save()
    messages.success(request, 'Status updated')
    if request.user.is_staff:
        return redirect('click:staff-bookings')
    else:
        return redirect('click:user-bookings')


def booking_comment(request):
    book = booking.objects.get(id=request.POST.get('booking_id'))
    serv = service.objects.get(id=request.POST.get('service_id'))
    comm = comments()
    comm.comment = request.POST.get('comment')
    comm.rating = request.POST.get('rate')
    comm.service = serv
    comm.booking = book
    comm.user = request.user
    comm.save()
    messages.success(request, 'Rating Posted Successfully')
    return redirect('click:user-bookings')


@user_passes_test(not_auth, 'click:user-dashboard', redirect_field_name='')
def loginView(request):
    return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# Authentication here.
def authLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if(user.is_superuser):
            return redirect('admin:index')
        else:
            return redirect('click:index')
    else:
        messages.error(request, 'Error Login')
        return redirect('click:login')


def authSignup(request):
    try:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        profil = profile()
        profil.dob = request.POST['date_of_birth']
        profil.mobile = request.POST['mob']
        profil.user = user
        profil.save()
        if user:
            login(request, user)
            return redirect('click:index')
        else:
            messages.error(request, 'Error Signup')
            return redirect('click:login')
    except:
        messages.error(request, 'Error Signup')
        return redirect('click:login')


def update_dp(request):
    pro = profile.objects.get(id=request.user.profile.id)
    pro.image = request.FILES.get('img')
    pro.save()
    if request.user.is_staff:
        return redirect('click:staff-profile')
    else:
        return redirect('click:user-profile')


def authLogout(request):
    logout(request)
    return redirect('click:index')


# User Routes
@login_required(login_url='click:login', redirect_field_name='')
def user(request):
    return redirect('click:user-dashboard')


@login_required(login_url='click:login', redirect_field_name='')
def userDashboard(request):
    return render(request, 'user/user-dashboard.html')


@login_required(login_url='click:login', redirect_field_name='')
def userBooking(request):
    bookings = booking.objects.filter(user=request.user).order_by('-id')
    return render(request, 'user/user-booking.html', {'bookings': bookings})


@login_required(login_url='click:login', redirect_field_name='')
def userProfile(request):
    return render(request, 'user/user-profile.html')


@login_required(login_url='click:login', redirect_field_name='')
def userReviews(request):
    reviews = comments.objects.filter(user=request.user)
    return render(request, 'user/user-reviews.html', {'reviews': reviews})


# Staff Routes
@login_required(login_url='click:login', redirect_field_name='')
def staff(request):
    return redirect('click:staff-dashboard')


@login_required(login_url='click:login', redirect_field_name='')
def staffDashboard(request):
    return render(request, 'staff/staff-dashboard.html')


@login_required(login_url='click:login', redirect_field_name='')
def staffBooking(request):
    bookings = booking.objects.filter(staff=request.user).order_by('-id')
    return render(request, 'staff/staff-booking.html', {'bookings': bookings})


@login_required(login_url='click:login', redirect_field_name='')
def staffProfile(request):
    return render(request, 'staff/staff-profile.html')
