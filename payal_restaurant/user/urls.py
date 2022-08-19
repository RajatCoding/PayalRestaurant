from django.urls import path
from user import views as user_views

urlpatterns = [
    

    path('login/', user_views.login_user, name='login'),
    path('signup/', user_views.signup_user, name='signup'),
    path('verifyotp/', user_views.verify_otp, name='otp'),
    path('userprofilehome/', user_views.user_profile_home, name='userprofilehome'),
    path('logout/', user_views.logout_user, name='logout'),
    path('profile/', user_views.user_profile, name='profile'),


]