from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views, user_login
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('base', views.base),
    path('', views.index,name='index'),
    path('about.html', views.about,name='about'),
    path('internships.html', views.internships,name='internships'),  
    path('accounts/', include('django.contrib.auth.urls')), 
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('doLogin', user_login.DO_LOGIN,name='doLogin'),
    path('home.html',views.home,name='home'),
    path('profile.html',views.PROFILE,name='profile'),
    path('profile.html/update',views.PROFILE_UPDATE,name="profile_update"),
    path('logout/', views.logout_view, name='logout'),
    path('contacts.html', views.contact_view, name='contact'),
    path('index.html', views.contact_index, name='contacts'),
    path('enrolledinternship.html', views.enrolledinternship,name='enrolledinternship'),
    path('<slug:slug>',views.INTERNSHIPS_DETAILS,name='internships_details'),
    path('enrolled-internships/', views.enrolledinternship, name='enrolled_internships'),
    path('<slug:slug>/', views.ENROLLEDCOURSE_DETAILS, name='enrolledcourse_details'),


] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
