import datetime

from django.db import models
from django.utils import timezone

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))


class BikeBrand(models.Model):
    brand_name = models.CharField(max_length=200)
    date_added = models.DateTimeField("date added")

    def __str__(self):
        return self.brand_name

    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_added <= now


class BikeModel(models.Model):
    brand_name = models.ForeignKey(BikeBrand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=200)
    model_year = models.IntegerField("year",  choices=YEAR_CHOICES,
                                     default=None)

    def __str__(self):
        return f"{self.model_year} {self.brand_name} {self.model_name}"


class BikeGeometry(models.Model):
    model_name = models.ForeignKey(BikeModel, on_delete=models.CASCADE)
    model_size = models.CharField(max_length=20)
    reach_mm = models.IntegerField(default=None)
    stack_mm = models.IntegerField(default=None)
    top_tube_effective_mm = models.IntegerField(default=None)
    seat_tube_center_top = models.IntegerField(default=None)
    head_angle_degrees = models.FloatField(default=None)
    seat_angle_degrees = models.FloatField(default=None)
    head_tube_length_mm = models.IntegerField(default=None)
    chainstay_length_mm = models.IntegerField(default=None)
    wheelbase_mm = models.IntegerField(default=None)
    front_center_mm = models.IntegerField(default=None)
    standover_mm = models.IntegerField(default=None)
    bb_drop_mm = models.IntegerField(default=None) 
    bb_height_mm = models.IntegerField(default=None) 
    bb_standard = models.CharField(max_length=20)
    fork_offset_mm = models.IntegerField(default=None) 
    trail_mm = models.IntegerField(default=None)
    seatpost_diameter_mm = models.IntegerField(default=None)
    seat_clamp_size = models.IntegerField(default=None)
    wheel_size = models.CharField(max_length=20)
    front_travel_mm = models.IntegerField(default=None)
    rear_travel_mm = models.IntegerField(default=None)
    socks_size = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.model_name} {self.model_size}"
