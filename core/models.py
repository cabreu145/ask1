from django.db import models

class CrudUser(models.Model):
    name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=25, blank=True)
    sells = models.IntegerField(blank=True, null=False)