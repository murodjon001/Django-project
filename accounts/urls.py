from django.urls import path
from . views import SignUpVW

urlpatterns = [
    path('signup', SignUpVW.as_view(), name='signup'),
]