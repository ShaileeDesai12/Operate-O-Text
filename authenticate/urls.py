from . import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt, csrf_protect

app_name = 'authenticate'
urlpatterns = [
    path('registration', views.register, name="registration"),
    path('login/', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]
