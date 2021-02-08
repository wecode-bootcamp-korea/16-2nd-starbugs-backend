import jwt, random

from .utils import classifier, input_file

from sklearn.preprocessing   import OrdinalEncoder

from django.test   import TestCase
from django.urls   import reverse

from starbugs.settings import SECRET
from user.models       import User
from product.models    import ( 
    Drink, 
    DrinkStatus, 
    MainCategory, 
    Size, 
    SubCategory, 
    Allergy,
)

class ProductListTest(TestCase):
    def setUp(self):
        self.list_url = reverse('list')
        self.maxDiff  = None

        self.user_test = User.objects.create(
            gender ='female',
            age    = '20-29',
            email  = "test@wecode.io",
        )
        main_category = MainCategory.objects.create(name="음료")
        SubCategory.objects.create(
                id            = 1,
                name          = 'test',
                description   = 'test',
                main_category = main_category
            )
        drink_status  = DrinkStatus.objects.create(name='강달쌘')
        
        for i in range(3):
            Drink.objects.create(
                id               = i + 1,
                sub_category     = SubCategory.objects.get(name='test'),
                korean_name      = 'abc',
                english_name     = 'abc',
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
    
    def test_list_get(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json(), 
        {
            'results': 
                [{
                    'subcategory_id': 1, 
                    'name': 'test', 
                    'description': 'test', 
                    'products': [{
                        'id': 1, 
                        'isnew': True, 
                        'isseason': True, 
                        'title': 'abc', 
                        'image': 'test.io', 
                        'size': 'Tall', 
                        'kcal': 1, 
                        'sodium': 2, 
                        'saturation': 2, 
                        'sugar': 10, 
                        'protein': 5, 
                        'caffeine': 5}, 
                        {
                        'id': 2, 
                        'isnew': True, 
                        'isseason': True, 
                        'title': 'abc', 
                        'image': 'test.io', 
                        'size': 'Tall', 
                        'kcal': 1, 
                        'sodium': 2, 
                        'saturation': 2, 
                        'sugar': 10, 
                        'protein': 5, 
                        'caffeine': 5}, 
                        {
                        'id': 3, 
                        'isnew': True, 
                        'isseason': True, 
                        'title': 'abc', 
                        'image': 'test.io', 
                        'size': 'Tall', 
                        'kcal': 1, 'sodium': 2, 
                        'saturation': 2, 
                        'sugar': 10, 
                        'protein': 5, 
                        'caffeine': 5}
                                       ]}]})
    
    def test_list_filter_get(self):
        response = self.client.get(self.list_url + '?name=test')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json(), {
            'results': 
            [
                {
                    'subcategory_id': 1, 
                    'name': 'test', 
                    'description': 'test', 
                    'products': [
                        {
                            'id': 1, 
                            'isnew': True, 
                            'isseason': True, 
                            'title': 'abc', 
                            'image': 'test.io', 
                            'size': 'Tall', 'kcal': 1, 
                            'sodium': 2, 'saturation': 2, 
                            'sugar': 10, 
                            'protein': 5, 
                            'caffeine': 5
                        }, 
                        {
                            'id': 2, 
                            'isnew': True, 
                            'isseason': True, 
                            'title': 'abc', 
                            'image': 'test.io', 
                            'size': 'Tall', 
                            'kcal': 1, 
                            'sodium': 2, 
                            'saturation': 2, 
                            'sugar': 10, 
                            'protein': 5, 
                            'caffeine': 5
                        }, 
                        {
                            'id': 3, 
                            'isnew': True, 
                            'isseason': True, 
                            'title': 'abc', 
                            'image': 'test.io', 
                            'size': 'Tall', 
                            'kcal': 1, 
                            'sodium': 2, 
                            'saturation': 2, 
                            'sugar': 10, 
                            'protein': 5, 
                            'caffeine': 5
                        }
                    ]
                }
            ]
        })
        

class MainSliderLoginTest(TestCase):
    def setUp(self):
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

        for i, sub in enumerate(subcategory_test_list):
            SubCategory.objects.create(
                id            = i + 1,
                name          = sub,
                description   = 'test',
                main_category = main_category
            )
        drink_status  = DrinkStatus.objects.create(name='강달쌘')
        test_drink_name = ['a', 'b', 'c']
        
        for i in range(50):
            Drink.objects.create(
                id               = i + 1,
                sub_category     = SubCategory.objects.get(name=random.choice(subcategory_test_list)),
                korean_name      = random.choice(test_drink_name),
                english_name     = random.choice(test_drink_name),
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
                size       = size,
                kcal       = 1, 
                sodium     = 2, 
                saturation = 2, 
                sugar      = 10, 
                protein    = 5, 
                caffeine   = 5
            )
            drink.allergies.add(*list(Allergy.objects.all()))
        
        token        = jwt.encode({'user_id':self.user_test.id}, SECRET, algorithm='HS256')
        self.headers = {"HTTP_Authorization" : token}
    
    def test_login_slider_get(self):
        response = self.client.get(self.slider_url, **self.headers, content_type='application/json')
        clf = classifier(input_file)
        
        X   = [[self.user_test.age, self.user_test.gender]]
        enc = OrdinalEncoder()
        enc.fit(X)
        OrdinalEncoder()
        X   = enc.transform(X)

        subcategory_predicted = clf.predict(X)[0]
        drinks                = Drink.objects.filter(sub_category=subcategory_predicted)
        
        test = list(response.json().keys())[0]
        self.assertEquals(test, 'my_urls')
        self.assertEquals(response.status_code, 200)
    
    def test_not_login_slider_get(self):
        response = self.client.get(self.slider_url)
        
        test = list(response.json().keys())[0]
        self.assertEquals(test, 'my_urls')
        self.assertEquals(response.status_code, 200)