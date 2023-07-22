from django.urls import path

from . import views

app_name = "bike_geometry"
urlpatterns = [
    path("", views.index, name="bike_list"),
    path("search/", views.search, name="search"),
    path("search/<int:id>/", views.bike_detail, name="detail"),
]
