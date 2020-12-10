from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.db.models import Count

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
    serviceData = service.objects.get(id=id)
    relateds = service.objects.filter(
        category=serviceData.category.id).exclude(id=serviceData.id)
    return render(request, 'service.html', {'service': serviceData, 'relateds': relateds})


def book_service(request):
    return render(request, 'book-service.html')


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
        return redirect('click:login')


def authSignup(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    # mobile = request.POST['mobile']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    if user:
        login(request, user)
        return redirect('click:index')
    else:
        return redirect('click:login')


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
    return render(request, 'user/user-booking.html')


@login_required(login_url='click:login', redirect_field_name='')
def userProfile(request):
    return render(request, 'user/user-profile.html')


@login_required(login_url='click:login', redirect_field_name='')
def userReviews(request):
    return render(request, 'user/user-reviews.html')


# Staff Routes
@login_required(login_url='click:login', redirect_field_name='')
def staff(request):
    return redirect('click:staff-dashboard')


@login_required(login_url='click:login', redirect_field_name='')
def staffDashboard(request):
    return render(request, 'staff/staff-dashboard.html')


@login_required(login_url='click:login', redirect_field_name='')
def staffBooking(request):
    return render(request, 'staff/staff-booking.html')


@login_required(login_url='click:login', redirect_field_name='')
def staffProfile(request):
    return render(request, 'staff/staff-profile.html')