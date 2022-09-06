from django.urls import path
from .views import PostDetailView,HomePageViev,BlogCreateVW, UpdatePostVW, DeletePostVW, SignUpVW
# PostElonVW, PostElonHome,
urlpatterns = [
    path('post/new', BlogCreateVW.as_view(), name='post_new'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post_detail'),
    # path('post/bulim/', PostElonHome.as_view(), name='post_bulim'),
    # path('post_elon/<int:pk>/', PostElonVW.as_view(), name='elon'),
    path('post/edit/<int:pk>/', UpdatePostVW.as_view(), name= 'post_edit'),
    path('post/delete/<int:pk>/', DeletePostVW.as_view(), name= 'post_delete'),
    path('', HomePageViev.as_view(), name="home"),
    path('signup', SignUpVW.as_view(), name='signup'),

]