from django.urls import path

from .views import  *

urlpatterns = [
    path('home',home,name="home"),
    path('signup/', signup, name='signup'),
    path('', sys_login, name='login'),
    path('logout/', handleLogout, name="logout "),
    path('blog/<slug:url>',post),
    path('category/<slug:url>',category),
]
