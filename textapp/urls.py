from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home),
    path('analyze',views.Analize),
    path('about',views.About),
    path('contact',views.Contact),
]