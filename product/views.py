from django.http      import JsonResponse
from django.views     import View

from .models          import Drink

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            drink = Drink.objects.prefetch_related("allergies","nutritions__size").get(id = product_id)

            product_info = {
                "id"                : product_id,
                "sub_category_name" : drink.sub_category.name,
                "korea_name"        : drink.korean_name,
                "english_name"      : drink.english_name,
                "main_description"  : drink.main_description,            
                "sub_description"   : drink.sub_description,
                "img_url"           : drink.image_url,
                "feel"              : drink.feel,
                "taste"             : drink.taste,
                "size" : [{
                    "size_id"     : nutrition.size.id,
                    "size_name"   : nutrition.size.name,
                    "price"       : int(drink.price) if nutrition.size.name == "Tall(톨)" else int(drink.price) * 1.5,
                    "nutritions" : {
                        "kcal"       : nutrition.kcal,
                        "sodium"     : nutrition.sodium,
                        "saturation" : nutrition.saturation,
                        "sugar"      : nutrition.sugar,
                        "protein"    : nutrition.protein,
                        "caffeine"   : nutrition.caffeine,
                    }   
                } for nutrition in drink.nutritions.all()],

                "allergies" : [{
                    "allergy_id"   : allergy.id,
                    "allergy_name" : allergy.name,
                } for allergy in drink.allergies.all()]
            }
            return JsonResponse({'item' : [product_info]}, status = 200)

        except Drink.DoesNotExist:
            return JsonResponse({'error' : "DRINK_DOES_NOT_EXIST"}, status=400)