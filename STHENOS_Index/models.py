from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import pytz

class User(AbstractUser):
    benchMax = models.IntegerField(null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )
    squatMax = models.IntegerField(null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )
    deadLiftMax = models.IntegerField(null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )
    age = models.IntegerField(null=True, blank=True,
        validators=[MinValueValidator(10), MaxValueValidator(100)]
    )
    height = models.IntegerField(null=True, blank=True,
        validators=[MinValueValidator(50), MaxValueValidator(300)]
    )
    weight = models.IntegerField(null=True, blank=True,
        validators=[MinValueValidator(10), MaxValueValidator(300)]
    )
    wristC = models.IntegerField(null=True, blank=True,
        validators=[MinValueValidator(5), MaxValueValidator(60)]
    )
    ankleC = models.IntegerField(null=True, blank=True,
        validators=[MinValueValidator(5), MaxValueValidator(60)]
    )
    bodyFat = models.IntegerField(null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(80)]
    )
    timezone = models.CharField(max_length=63, default='UTC')

    def get_localized_timestamp(self, timestamp):
        # Convert the timestamp to the user's timezone
        local_tz = pytz.timezone(self.timezone)
        return timestamp.astimezone(local_tz)