from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test


# Test Functions
def is_admin(user):
    return user.is_superuser


# Create your views here.
@user_passes_test(is_admin, 'click:login', redirect_field_name='')
def index(request):
    return render(request, 'admin/index.html')
