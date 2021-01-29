from django.views     import View
from django.http      import JsonResponse

from .models          import Drink

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            drink = Drink.objects.prefetch_related("allergies").get(id = product_id)

            product_info = {
                "id"                : product_id,
                "sub_category_name" : drink.sub_category.name,
                "korea_name"        : drink.korean_name,
                "english_name"      : drink.english_name,
                "main_description"  : drink.main_description,            
                "sub_description"   : drink.sub_description,
                "price"             : drink.price,
                "img_url"           : drink.image_url,
                "feel"              : drink.feel,
                "destiny"           : drink.destiny,
                "taste"             : drink.taste,
                "size" : [{
                    "size_id"     : nutrition.size.id,
                    "size_name"   : nutrition.size.name,
                    "nutrtitions" : {
                        "kcal"       : nutrition.kcal,
                        "sodium"     : nutrition.sodium,
                        "saturation" : nutrition.saturation,
                        "sugar"      : nutrition.sugar,
                        "protein"    : nutrition.protein,
                        "caffeine"   : nutrition.caffeine,
                    }   
                } for nutrition in drink.nutritions.select_related("size")],

                "allergies" : [{
                    "allergy_id"   : allergy.id,
                    "allergy_name" : allergy.name,
                } for allergy in drink.allergies.all()]
            }
            return JsonResponse({'product' : product_info}, status = 200)

        except Drink.DoesNotExist:
            return JsonResponse({'error' : "Drink does not exist"}, status=400)