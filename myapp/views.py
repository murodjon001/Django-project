from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models.users import Post
# from .models.post_elon import PostElon #!!!!
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic



# Create your views here.

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
#
# class PostElonHome(ListView):
#     model = PostElon
#     template_name = 'elon_bulim.html'
#     context_object_name = 'elon_uchun'

class HomePageViev(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'default'

class BlogCreateVW(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','author', 'body',]

class UpdatePostVW(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']
#
class DeletePostVW(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

# class PostElonVW(DetailView):
#     model = PostElon
#     template_name = 'elon.html'


class SignUpVW(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



#
# def add_post(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         author = request.POST['author']
#         body = request.POST['body']
#
#         if len(title) < 3:
#             return HttpResponse('Mavzu nomi juda kichik')
#         elif len(author) < 1:
#             return HttpResponse('Muallif nomi juda kichik')
#         elif len(body) == 0:
#             return HttpResponse('Mavzuga matn kiriting')
#         else:
#             newpost = Post(title = title, author = author, body = body)
#             print(newpost)
#             newpost.save()
#     return render(request, 'post_new.html')
