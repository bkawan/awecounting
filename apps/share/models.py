from django.db import models
import datetime
from njango.fields import today, BSDateField
from apps.users.models import Company


class ShareHolder(models.Model):
    name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name


class Collection(models.Model):
    count = models.PositiveIntegerField()
    interest_rate = models.FloatField()
    start_date = BSDateField(blank=True, null=True, default=today)
    end_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey(Company)

    def __str__(self):
        return str(self.count)

    def get_class_name(self):
        return self.__class__.__name__


class Investment(models.Model):
    share_holder = models.ForeignKey(ShareHolder)
    date = models.DateField(default=datetime.date.today)
    amount = models.FloatField()
    collection = models.ForeignKey(Collection)
