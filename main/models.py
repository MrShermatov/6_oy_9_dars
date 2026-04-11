
from django.db import models

class Models(models.Model):
    model_name = models.CharField(max_length=1000)
    brand_loga = models.ImageField(upload_to='images/', blank=True, null=True)
    brand_countr = models.CharField(max_length=100)

    def __str__(self):
        return f"Model {self.model_name}"

class Cars(models.Model):
    car_name = models.CharField(max_length=100, unique=True)
    car_year = models.DateField(blank=True, null=True)
    car_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    car_color = models.CharField(max_length=100)
    car_description = models.TextField(blank=True, null=True)
    car_image = models.ImageField(upload_to='images/', blank=True, null=True)
    create_car = models.DateTimeField(auto_now_add=True)
    update_car = models.DateTimeField(auto_now=True)
    car_model = models.ForeignKey(Models,
                                  on_delete=models.CASCADE,
                                  verbose_name="Mashina modeli")
