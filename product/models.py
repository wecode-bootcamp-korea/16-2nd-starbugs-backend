from django.db import models

class MainCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "maincategories"


class SubCategory(models.Model):
    name          = models.CharField(max_length=50)
    description   = models.CharField(max_length=200, null=True)
    main_category = models.ForeignKey('MainCategory', on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        db_table = "subcategories"


class Drink(models.Model):
    sub_category      = models.ForeignKey('SubCategory', on_delete=models.CASCADE, related_name='drinks')
    korean_name       = models.CharField(max_length=50)
    english_name      = models.CharField(max_length=50)
    main_description  = models.TextField()
    sub_description   = models.TextField()
    created_at        = models.DateTimeField(auto_now_add=True)
    is_new            = models.BooleanField()
    is_season         = models.BooleanField()
    density           = models.IntegerField(default=0)
    taste             = models.IntegerField(default=0)
    feel              = models.IntegerField(default=0)
    price             = models.DecimalField(max_digits=10, decimal_places=4)
    image_url         = models.URLField()
    allergies         = models.ManyToManyField('Allergy', through="DrinkAllergy")
    drink_status      = models.ForeignKey('DrinkStatus', on_delete=models.CASCADE, related_name='drinks')

    class Meta:
        db_table = "drinks"


class Allergy(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "allergies"


class DrinkAllergy(models.Model):
    drink   = models.ForeignKey('Drink', on_delete=models.CASCADE)
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE) 

    class Meta:
        db_table = "drinkallergies"


class Size(models.Model):
    name = models.CharField(max_length=50, null=True)
    
    class Meta:
        db_table = "sizes"


class Nutrition(models.Model):
    drink      = models.ForeignKey('Drink', on_delete=models.CASCADE, related_name="nutritions")
    size       = models.ForeignKey('Size', on_delete=models.CASCADE, related_name="nutritions")
    kcal       = models.IntegerField()
    sodium     = models.IntegerField()
    saturation = models.IntegerField()
    sugar      = models.IntegerField()
    protein    = models.IntegerField()
    caffeine   = models.IntegerField()

    class Meta:
        db_table = "nutritions"


class DrinkStatus(models.Model):
    name = models.CharField(max_length=50)  

    class Meta:
        db_table = "drinkstatus"
        