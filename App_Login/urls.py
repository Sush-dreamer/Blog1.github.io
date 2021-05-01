from django.urls import path
from App_Login import views

app_name='App_Login'

urlpatterns = [

    path('signup/',views.sing_up,name='signup'),
    path('signin/',views.login_page,name='signin'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('updated-profile/',views.user_change,name='updatedprofile'),
    path('password/',views.pass_change,name='pass_change'),
    path('change-profile-image/',views.add_pro_pic,name='add_pro_pic'),
    path('change-picture/',views.change_pro_pic,name='change_pro_pic'),
    

]


