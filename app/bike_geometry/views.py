from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import BikeBrand, BikeModel, BikeGeometry


class IndexView(generic.ListView):
    template_name = "bike_geometry/index.html"
    context_object_name = "latest_brand_list"

    def get_queryset(self):
        """
        Return the last five published bike brands
        (not including those set to be published 
        in the future).
        """
        return BikeBrand.objects.filter(date_added__lte=timezone.now()).order_by("-date_added")[
            :5
        ]
