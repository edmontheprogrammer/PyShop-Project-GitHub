from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


# Create a new model  Named 'Offer'
# with the following fields
# - code text filed
# - description text filed
# - discount floating point (0.2)
# - create a migration to update the database
# and make the changes
class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=600)
    discount = models.FloatField(max_length=2)
