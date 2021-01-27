from django.db import models

class User(models.Model):  
    drink_propensity = models.JSONField()
    sex              = models.CharField(max_length=50)
    age              = models.IntegerField()
    email            = models.CharField(max_length=100)

    class Meta:
        db_table = "users"


class UserDrinkStatus(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_drink_statuses")
    name = models.CharField(max_length=50)  

    class Meta:
        db_table = "user_drink_statuses"

