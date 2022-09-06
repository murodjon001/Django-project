from django.contrib import admin
from . models.users import Post
# from .models.post_elon import PostElon    #!!!!
# from .models.users import CustomUser1
# from django.contrib.auth.admin import UserAdmin
# from .form import CustomUserChangeForm,CustomCreateForm
# from . models.users import CustomUser1
# # Register your models here.
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email','username','age','adress','nickname']
#
# admin.site.register(CustomUser,CustomUserAdmin)
#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomCreateForm
#     form = CustomUserChangeForm
#     model = CustomUser1
#     list_display = ['email','username','age','adress','job']
#
# admin.site.register(CustomUser1,CustomUserAdmin)
admin.site.register(Post)
# admin.site.register(PostElon)  # !!!!



