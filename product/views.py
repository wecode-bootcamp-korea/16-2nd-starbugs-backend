import random
import numpy as np

from django.views import View
from django.http  import JsonResponse

from sklearn.preprocessing   import OrdinalEncoder
from sklearn.naive_bayes     import CategoricalNB

from .utils      import classifier, create_order_data, input_file
from user.utils  import check_user_slider
from user.models import User
from .models     import (
    MainCategory, 
    SubCategory,
    Drink,
    Allergy,
    DrinkAllergy,
    Size,
    Nutrition,
    DrinkStatus
)


class DrinkListView(View):
    def get(self, request):
        names            = request.GET.get("name", None)
        filter_set       = {}

        if names:
            filter_set['name__in'] = names.split(',')
           
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

class MainSlideProductsView(View):
    def classifier(input_file):
        df = pd.read_csv(input_file, header = 0)
        X = df.iloc[:, :2].to_numpy()
        y = df.iloc[:, 2].to_numpy()

        enc = OrdinalEncoder()
        enc.fit(X)
        OrdinalEncoder()

        le = preprocessing.LabelEncoder()
        le.fit(y)
        preprocessing.LabelEncoder()

        X = enc.transform(X)
        y = le.transform(y)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        clf = CategoricalNB()
        classifier = clf.fit(X_train, y_train)
        
        return classifier

    @check_user_slider
    def get(self, request):
        if request.user:
            clf  = classifier(input_file)
            user = request.user

            enc = OrdinalEncoder()
            X   = np.array([[user.age, user.gender]])
            enc.fit(X)
            OrdinalEncoder()
            X   = enc.transform(X)

            subcategory_predicted = int(clf.predict(X)[0])

            drinks = Drink.objects.filter(sub_category=SubCategory.objects.get(id=subcategory_predicted+1))
            urls   = [drink.image_url for drink in drinks]
            return JsonResponse({
                "my_urls": urls
            }, status=200)
        else:
            print(SubCategory.objects.values_list('id'))
            drinks = Drink.objects.filter(sub_category=SubCategory.objects.get(id=random.randint(1, 9)))
            urls   = [drink.image_url for drink in drinks]
            return JsonResponse({
                "my_urls": urls 
            }, status=200)

