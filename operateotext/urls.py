from django.urls import path
from . import views

app_name = 'operateotext'
urlpatterns = [
    path('', views.index, name='index'),
    path('tools', views.tools, name='tools'),
    path('input/<text>/', views.input, name='input'),
    path('feedback', views.feedback, name='feedback'),
]
