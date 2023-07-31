import datetime

from django.db import models
from django.utils import timezone

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year + 1)):
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
    model_year = models.IntegerField("year", choices=YEAR_CHOICES,
                                     default=datetime.datetime.now().year)

    def __str__(self):
        return f"{self.model_year} {self.brand_name} {self.model_name}"


class BikeGeometry(models.Model):
    class Wheelsize(models.TextChoices):
        size_20_inch = 0, '20"'
        size_24_inch = 1, '24"'
        size_26_inch = 2, '26"'
        size_275_inch = 3, '27.5"'
        size_29_inch = 4, '29"'

    model_name = models.ForeignKey(BikeModel, on_delete=models.CASCADE)
    model_size = models.CharField(max_length=20)
    reach_mm = models.IntegerField(default=None, blank=True, null=True)
    stack_mm = models.IntegerField(default=None, blank=True, null=True)
    top_tube_effective_mm = models.IntegerField(default=None, blank=True, null=True)
    seat_tube_center_top = models.IntegerField(default=None, blank=True, null=True)
    head_angle_degrees = models.FloatField(default=None, blank=True, null=True)
    seat_tube_angle_degrees = models.FloatField(default=None, blank=True, null=True)
    head_tube_length_mm = models.IntegerField(default=None, blank=True, null=True)
    chainstay_length_mm = models.IntegerField(default=None, blank=True, null=True)
    wheelbase_mm = models.IntegerField(default=None, blank=True, null=True)
    front_center_mm = models.IntegerField(default=None, blank=True, null=True)
    standover_mm = models.IntegerField(default=None, blank=True, null=True)
    bb_drop_mm = models.IntegerField(default=None, blank=True, null=True)
    bb_height_mm = models.IntegerField(default=None, blank=True, null=True)
    bb_standard = models.CharField(max_length=20, blank=True, null=True)
    fork_offset_mm = models.IntegerField(default=None, blank=True, null=True)
    trail_mm = models.IntegerField(default=None, blank=True, null=True)
    seatpost_diameter_mm = models.IntegerField(default=None, blank=True, null=True)
    seat_clamp_size = models.IntegerField(default=None, blank=True, null=True)
    wheel_size = models.CharField(
        max_length=20,
        choices=Wheelsize.choices,
        blank=True,
        null=True,
    )
    front_travel_mm = models.IntegerField(default=None, blank=True, null=True)
    rear_travel_mm = models.IntegerField(default=None, blank=True, null=True)
    shock_size = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.model_name} {self.model_size}"
