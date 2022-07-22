
from django.urls import path
from user import views as user_views

urlpatterns = [
   
    path('login/', user_views.login_user, name='login'),
    path('signup/', user_views.signup_user, name='signup'),
  


]
