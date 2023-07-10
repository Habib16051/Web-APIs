from django.urls import path
from . import views
# app name

app_name = 'books'

urlpatterns = [
    path('', views.ListBook.as_view(), name="home"),


]
