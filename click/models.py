from django.db import models
from django.db import connections
from django.contrib.auth.models import User
from PIL import Image
from django.utils.timezone import now


class category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='category', default='SOME STRING')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Categories"


class service(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='service', default='SOME STRING')
    description = models.TextField()
    feature = models.CharField(max_length=200)
    price = models.IntegerField(default=10)
    category = models.ForeignKey(category,  on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class booking(models.Model):
    booking_date = models.DateTimeField(auto_now_add=True, editable=False)
    date = models.DateField(default=now,blank=True, null=True)
    time = models.TimeField(default=now)
    location = models.TextField()
    phn = models.BigIntegerField(verbose_name="Phone Number")
    staff = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='staff', null=True, blank=True)
    status = models.CharField(max_length=256, default='Pending', choices=[('Pending', 'Pending'), (
        'Staff assigned', 'Staff assigned'), ('In progress', 'In progress'), ('Completed', 'Completed'), ('Canceled', 'Canceled')])
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    reason= models.TextField(null=True,blank=True)
    payment_id = models.TextField(default='nil')

    def __str__(self):
        return f"{self.user.first_name} - {self.service.title}"



class comments(models.Model):
    comment = models.TextField()
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    booking = models.OneToOneField(booking, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Review"

class profile(models.Model):
    image = models.ImageField(upload_to='profile', default='profile/profile.png')
    mobile = models.BigIntegerField(verbose_name="Phone Number")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob=models.DateField(default=now,blank=True, null=True)
    

