from django.db import models

class User(models.Model):  
    gender       = models.CharField(max_length=50)
    age          = models.CharField(max_length=50)
    email        = models.CharField(max_length=100)
    density      = models.IntegerField(default=0)
    taste        = models.IntegerField(default=0)
    feel         = models.IntegerField(default=0)
    drink_status = models.ForeignKey('product.DrinkStatus', on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        db_table = "users"