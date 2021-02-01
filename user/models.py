from django.db import models

class User(models.Model):  
    gender           = models.CharField(max_length=50)
    age              = models.CharField(max_length=50)
    email            = models.CharField(max_length=100)
    drink_status     = models.ForeignKey('product.DrinkStatus')
    
    class Meta:
        db_table = "users"
