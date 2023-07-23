from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Q
import django_tables2 as tables
from django_pandas.io import read_frame
import django_pandas as dpd
import pandas as pd

from .models import BikeBrand, BikeModel, BikeGeometry


def index(request):
    bike = BikeModel.objects.all()
    return render(request, "bike_geometry/index.html", {"bike": bike})


def bike_detail(request, id):
    bike = get_object_or_404(BikeModel, id=id)
    geo = get_object_or_404(BikeGeometry, model_name_id=id)
    queryset = BikeGeometry.objects.all()

    df = dpd.io.read_frame(queryset)
    df.rename(columns=lambda x: x.replace("_", " "), inplace=True)
    df = df.drop(columns=['id'])
    df = df.set_index('model name').T.reset_index()
    
    table = df.style.set_table_attributes('class="table table-striped"').to_html(
        index=True
    )

    return render(
        request,
        "bike_geometry/bike_detail.html",
        {"bike": bike, "geo": geo, "table": table},
    )


def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get("search")
        if query == "" or query is None:
            query = "None"

        results = BikeModel.objects.filter(
            Q(brand_name__brand_name__icontains=query) | Q(model_name__icontains=query)
        )

    return render(
        request,
        "bike_geometry/search_results.html",
        {"query": query, "results": results},
    )
