from django.db import models

class MainCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "maincategories"


class SubCategory(models.Model):
    name          = models.CharField(max_length=50)
    description   = models.CharField(max_length=200)
    main_category = models.ForeignKey('MainCategory', on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        db_table = "subcategories"


class Drink(models.Model):
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE, related_name='drinks')
    korean_name  = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)
    description  = models.TextField()
    created_at   = models.DateField(auto_now_add=True)
    destiny      = models.IntegerField()
    is_new       = models.BooleanField()
    is_season    = models.BooleanField()
    allergies    = models.ManyToManyField('Allergy', through="DrinkAllergy")
    tastes       = models.ManyToManyField('Taste', through="DrinkTaste")
    feels        = models.ManyToManyField('Feel', through="DrinkFeel")

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


class Taste(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "tastes"


class DrinkTaste(models.Model):
    drink   = models.ForeignKey('Drink', on_delete=models.CASCADE)
    taste   = models.ForeignKey('Taste', on_delete=models.CASCADE)

    class Meta:
        db_table = "drinktastes"


class Feel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "feels"

class DrinkFeel(models.Model):
    drink   = models.ForeignKey('Drink', on_delete=models.CASCADE)
    feel    = models.ForeignKey('Feel', on_delete=models.CASCADE)

    class Meta:
        db_table = "drinkfeels"

class Image(models.Model):
    image_url = models.URLField(max_length=200)
    drink   = models.ForeignKey('Drink', on_delete=models.CASCADE, related_name='drinks')

    class Meta:
        db_table = "images"


class Size(models.Model):
    ounce_size = models.CharField(max_length=50)
    cup_size   = models.CharField(max_length=50)

    class Meta:
        db_table = "sizes"


class Nutrition(models.Model):
    drink      = models.ForeignKey('Drink', on_delete=models.CASCADE, related_name="nutritions")
    size       = models.ForeignKey('Size', on_delete=models.CASCADE, related_name="nutritions")
    kcal       = models.DecimalField(max_digits=10, decimal_places=2)
    sodium     = models.DecimalField(max_digits=10, decimal_places=2)
    saturation = models.DecimalField(max_digits=10, decimal_places=2)
    sugar      = models.DecimalField(max_digits=10, decimal_places=2)
    protein    = models.DecimalField(max_digits=10, decimal_places=2)
    caffeine   = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "nutritions"


