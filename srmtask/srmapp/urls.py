from django.urls import path
from django import urls
from django.conf.urls import url
from . import views
from django.conf import settings
# from django.conf.urls.static import static

urlpatterns=[
		path('',views.home,name="home"),
		path('signup/',views.signup,name='signup'),
		path('login/',views.login,name='login'),
		path('save_user/',views.save_user,name="save_user"),
		path('login_check/',views.login_check,name="login_check"),
		path('org_show/',views.org_show,name="org_show"),
		# path('logout/',views.logout,name="logout")

] 

