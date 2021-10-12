from django.urls import path
from . import views

app_name  = 'App_Login'

urlpatterns = [
    path('signup/', views.signup, name = "signup"),
    path('signin/', views.login_page, name = 'signin'),
    path('logout/' , views.logout_user, name = "logout" ),
    path('profile/' , views.profile, name = "profile" ),
    path('change-profile/' , views.user_change, name = "user_change" ),
    path('password/' , views.pass_change, name = "pass_change" ),
    path('changeprofileimage/' , views.add_pro_pic, name = "add_pro_pic"),
    path('change-picture/' , views.change_pro_pic, name = "change_pro_pic"),

]