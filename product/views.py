import random
import numpy as np

from django.views import View
from django.http  import JsonResponse

from sklearn.preprocessing   import OrdinalEncoder

from .utils      import classifier, input_file
from user.utils  import check_user_slider, query_debugger
from .models     import SubCategory, Drink


class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            drink = Drink.objects.prefetch_related("allergies", "nutritions__size").get(id = product_id)

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

class DrinkListView(View):
    @query_debugger
    def get(self, request):
        names      = request.GET.get("name", None)
        filter_set = {}

        if names:
            filter_set['name__in'] = names.split(',')
           
        subcategory_list = [{
            'subcategory_id' : subcategory.id,
            'name'           : subcategory.name,
            'description'    : subcategory.description,
            'products' : [{
                'id'         : drink.id,
                'isnew'      : drink.is_new,
                'isseason'   : drink.is_season,
                'title'      : drink.korean_name,
                'image'      : drink.image_url,
                'size'       : drink.nutritions.first().size.name,
                'kcal'       : drink.nutritions.first().kcal,
                'sodium'     : drink.nutritions.first().sodium,
                'saturation' : drink.nutritions.first().saturation,
                'sugar'      : drink.nutritions.first().sugar,
                'protein'    : drink.nutritions.first().protein,
                'caffeine'   : drink.nutritions.first().caffeine
            } for drink in subcategory.drinks.all()]  
        } for subcategory in SubCategory.objects.prefetch_related('drinks__nutritions').filter(**filter_set)]

        return JsonResponse({"results" : subcategory_list}, status = 200)

class MainSlideProductsView(View):
    @check_user_slider
    def get(self, request):
        if request.user:
            user = request.user
            clf  = classifier(input_file)

            enc = OrdinalEncoder()
            X   = np.array([[user.age, user.gender]])
            enc.fit(X)
            OrdinalEncoder()
            X   = enc.transform(X)

            subcategory_predicted = clf.predict(X)[0]
            
            drinks = Drink.objects.filter(sub_category=SubCategory.objects.get(id=subcategory_predicted+1))
            urls   = [drink.image_url for drink in drinks]
            return JsonResponse({"my_urls": urls}, status=200)
        
        drinks = Drink.objects.filter(sub_category=SubCategory.objects.get(id=random.randint(1, 9)))
        urls   = [drink.image_url for drink in drinks]
        return JsonResponse({"my_urls": urls }, status=200)
        