from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('signup1/',views.signup1,name='signup1'),
    path('login1/',views.login1,name='login1'),
    path('logout/',views.logout,name='logout'),
    path('contact/',views.contact,name='contact'),
    
]