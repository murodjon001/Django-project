from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    surmane = models.CharField(max_length=60)
    age = models.IntegerField()
    birthdate = models.DateField()
    phone = models.CharField(max_length=13)
    image = models.ImageField()


class Post(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        get_user_model(),
        on_delete= models.CASCADE
    )
    body = models.TextField()
    image = models.ImageField(null=False, blank=True, upload_to= 'media/images')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

# Create your models here.
# class CustomUser1(AbstractUser):
#     age = models.PositiveIntegerField(null=True,blank=True)
#     adress = models.CharField(max_length=80)
#     job = models.CharField(max_length=55)

