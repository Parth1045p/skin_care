from django.urls import path
from . import views

urlpatterns=[
  path('',views.home,name='homi'),
  path('register/',views.register_page,name='regi'),
  path('login/',views.login_page,name='logi'),
  path('dashboard/',views.dash_board,name='dash'),
  path('logout/',views.log_out,name='logout'),
]