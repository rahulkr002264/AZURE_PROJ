from django.urls import path
from myapp1 import views

urlpatterns = [
    path('homepage/', views.homepage),
    path('new_registration/', views.newuser),
    path('new_registration_detail/', views.newuser_detail),
    path('login/', views.loginForm),
    path('login1/', views.login1),
    path('logout1/', views.logout1),
    path('d_register/', views.d_register_form),
    path('p_register/', views.p_register_form),
    path('d_reg_detail/', views.d_registration),
    path('p_reg_detail/', views.p_registration),
    path('history/', views.historyForm),
    path('mydetails/', views.mydetails),

]
