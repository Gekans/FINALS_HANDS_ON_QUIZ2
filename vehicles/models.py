from django.db import models


class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    price = models.FloatField()

    def _format_price(self):
        return f"{self.price:g}"

    def vehicle_info(self):
        return f"{self.brand} costs {self._format_price()}"


class Car(Vehicle):
    doors = models.IntegerField()

    def vehicle_info(self):
        return f"{self.brand} Car with {self.doors} doors costs {self._format_price()}"


class Motorcycle(Vehicle):
    helmet_included = models.BooleanField(default=False)

    def vehicle_info(self):
        return f"{self.brand} Motorcycle costs {self._format_price()}"
