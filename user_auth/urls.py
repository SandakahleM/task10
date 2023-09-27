from django.urls import path
from . import views

# provide app name
app_name = 'user_auth'


urlpatterns = [

    path('login', views.user_login, name="login"),
    path('logout_user', views.logout_user, name='logout'),
    #path('authenticate_user/', views.authenticate, name='authenticate_user'),
    path('register_user/', views.register_user, name='register_user'),
   

]
