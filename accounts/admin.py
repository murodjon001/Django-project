from django.contrib import admin
from .models import CustomUser
from .form import CustomCreationForm,CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username','age','adress','job']
admin.site.register(CustomUser,CustomUserAdmin)
