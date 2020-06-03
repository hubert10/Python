from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}  - {}".format(self.name, self.price)