from django.urls import path

from . import views

app_name = "bike_geometry"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('list/', views.bike_list, name='bike_list'),
    path('search/', views.search, name='search'),
   
]