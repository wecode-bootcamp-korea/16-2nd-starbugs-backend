import json

from django.views   import View
from django.http    import JsonResponse

from product.models import Drink, SubCategory, Nutrition

class DrinkListView(View):
    def get(self, request):
        names            = request.GET.getlist("name", None)
        filter_set       = {}

        if names:
            filter_set['name__in'] = names
            
        subcategory_list = [
        {
        'subcategory_id' : subcategory.id,
        'name'           : subcategory.name,
        'description'    : subcategory.description,
        'products' : [
            {
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
        }for subcategory in SubCategory.objects.prefetch_related('drinks__nutritions').filter(**filter_set)]

        return JsonResponse({"results" : subcategory_list}, status = 200)