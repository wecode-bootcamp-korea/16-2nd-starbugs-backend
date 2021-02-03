import jwt, random

from .utils import classifier, input_file

from sklearn.preprocessing   import OrdinalEncoder
from sklearn.naive_bayes     import CategoricalNB

from django.test   import TestCase, Client
from django.urls   import reverse

from starbugs.settings import SECRET
from user.models       import User
from product.models    import ( 
    Drink, 
    DrinkStatus, 
    MainCategory, 
    Size, 
    SubCategory, 
    Nutrition, 
    DrinkAllergy,
    Allergy,
)


class ProductListTest(TestCase):
    def setUp(self):
        self.list_url = reverse('list')
    
    def test_list_get(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
    
    def test_list_filter_get(self):
        response = self.client.get(self.list_url + '?name=콜드브루, 브루드 커피')
        self.assertEquals(response.status_code, 200)
        
class MainSliderLoginTest(TestCase):
    def setUp(self):
        print("start setup")
        
        self.slider_url = reverse('slider')
        self.user_test  = User.objects.create(
            gender ='female',
            age    = '20-29',
            email  = "test@wecode.io",
        )

        subcategory_test_list = [
            'test1', 
            'test2', 
            'test3', 
            'test4', 
            'test5', 
            'test6',
            'test7',
            'test8',
            'test9'
            ]

        main_category = MainCategory.objects.create(name="음료")

        for sub in subcategory_test_list:
            SubCategory.objects.create(
                name          = sub,
                description   = 'test',
                main_category = main_category
            )
        print("subcategory count ::: ", SubCategory.objects.values_list('id'))
        drink_status  = DrinkStatus.objects.create(name='강달쌘')

        test_drink_name = ['a', 'b', 'c']
        
        for _ in range(50):
            Drink.objects.create(
                sub_category=SubCategory.objects.get(name=random.choice(subcategory_test_list)),
                korean_name=random.choice(test_drink_name),
                english_name=random.choice(test_drink_name),
                main_description = 'a',
                sub_description  = 'b',
                is_new           = True,
                is_season        = True,
                price            = 6000,
                density          = 20,
                taste            = 20,
                feel             = 20,
                drink_status     = drink_status,
                image_url        = 'test.io'
            )
        
        size = Size.objects.create(name='Tall')
       
        Allergy.objects.bulk_create([
            Allergy(name = '콩'),
            Allergy(name = '두유'),
        ])

        for allergy_name in ['콩', '두유']:
            allergy = Allergy.objects.create(name = allergy_name)

        for drink in Drink.objects.all():
            drink.nutritions.create(
                size = size,
                kcal       = 1, 
                sodium     = 2, 
                saturation = 2, 
                sugar      = 10, 
                protein    = 5, 
                caffeine   = 5
            )
            drink.allergies.add(*list(Allergy.objects.all()))
        
        token = jwt.encode({'user_id':self.user_test.id}, SECRET, algorithm='HS256')
        self.headers = {"HTTP_Authorization" : token}
    
    def test_login_slider_get(self):
        print("test_login_slider_get start")
        response = self.client.get(self.slider_url, **self.headers, content_type='application/json')
        
        X   = [[self.user_test.age, self.user_test.gender]]
        enc = OrdinalEncoder()
        enc.fit(X)
        OrdinalEncoder()
        X   = enc.transform(X)

        clf = classifier(input_file)
        subcategory_predicted = int(clf.predict(X)[0])
        print('@'*20)
        print('sub_pred', subcategory_predicted)
        drinks                = Drink.objects.filter(sub_category=subcategory_predicted)
        
        self.assertEquals(drinks[0].price, 6000.0000)
    
    # def test_not_login_slider_get(self):
    #     print("test_not_login_slider_get start")
    #     response = self.client.get(self.slider_url)
    #     urls = [drink.image_url for drink in Drink.objects.filter(
    #         sub_category=SubCategory.objects.get(id=random.randint(10, 18))
    #         )]
    #     self.assertEquals(urls[0], 'test.io')
    #     self.assertEquals(response.status_code, 200)

class MainSliderNoLoginTest(TestCase):
    def setUp(self):
        self.url = reverse('slider')
    
    def test_not_login_slider_get(self):
        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)


