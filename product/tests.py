from django.test    import TestCase, Client
from product.models import ( 
    Drink, 
    DrinkStatus, 
    MainCategory, 
    Size, 
    SubCategory, 
    Nutrition, 
)


client = Client()

class DrinkListTest(TestCase):
    maxDiff = None
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.category     = MainCategory.objects.create(name="음료")
        cls.coldbrew     = SubCategory.objects.create(name="콜드브루", description="우리 사랑하자", main_category=cls.category)
        cls.brudcoffee   = SubCategory.objects.create(name="브루드 커피", description="더 사랑하자", main_category=cls.category)
        cls.size_1       = Size.objects.create(name="Tall(톨)")
        cls.size_2       = Size.objects.create(name="regular(레귤러)") 
        cls.drink_status = DrinkStatus.objects.create(name="강달쎈")
        cls.nitro        = Drink.objects.create(
            sub_category = cls.coldbrew,
            korean_name  = "나이트로 바닐라 크림",
            english_name = "Nitro Vanilla Cream",
            main_description = "사랑해",
            sub_description = "더 사랑해",
            is_new       = True,
            is_season    = False,
            density      = 100,
            taste        = 100,
            feel         = 100,
            image_url    = "drink_image_url",
            price        = 1000,
            drink_status = DrinkStatus.objects.get(name="강달쎈"))

        cls.icecoffee  = Drink.objects.create(
            sub_category = cls.brudcoffee,
            korean_name  = "아이스 커피",
            english_name = "Iced Coffee",
            main_description = "사랑해",
            sub_description = "더 사랑해",
            is_new       = False,
            is_season    = False,
            density      = 100,
            taste        = 100,
            feel         = 100,
            image_url    = "drink_image_url",
            price        = 2000,
            drink_status = DrinkStatus.objects.get(name="강달쎈")
            )

        cls.nutrition   = Nutrition.objects.create(
            drink = cls.nitro,
            size  = cls.size_1,
            kcal     = 10,
            sodium = 15,
            saturation= 20,
            sugar = 25,
            protein = 30,
            caffeine = 35
            )

        cls.nutrition   = Nutrition.objects.create(
            drink = cls.nitro,
            size  = cls.size_2,
            kcal     = 20,
            sodium = 30,
            saturation= 40,
            sugar = 50,
            protein = 60,
            caffeine = 70
            )

        cls.nutrition   = Nutrition.objects.create(
            drink = cls.icecoffee,
            size  = cls.size_1,
            kcal     = 100,
            sodium = 150,
            saturation= 200,
            sugar = 250,
            protein = 300,
            caffeine = 350
            )

        cls.nutrition   = Nutrition.objects.create(
            drink = cls.icecoffee,
            size  = cls.size_2,
            kcal     = 200,
            sodium = 300,
            saturation= 400,
            sugar = 500,
            protein = 600,
            caffeine = 700
            )

    def tearDown(self):
        MainCategory.objects.all().delete()
        Drink.objects.all().delete()
        SubCategory.objects.all().delete()
        Size.objects.all().delete()
        Nutrition.objects.all().delete()

    def test_product_list_get_success(self):
        response = self.client.get('/product')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
        'results': [
            {
            'subcategory_id': 1, 
            'name': '콜드브루', 
            'description': '우리 사랑하자', 
            'products': [{
                'id': 1, 
                'isnew': True, 
                'isseason': False, 
                'title': '나이트로 바닐라 크림', 
                'image': 'drink_image_url', 
                'size': 'Tall(톨)', 
                'kcal': 10, 
                'sodium': 15, 
                'saturation': 20, 
                'sugar': 25, 
                'protein': 30, 
                'caffeine': 35
                }
            ]
        }, 
            {
            'subcategory_id': 2, 
            'name': '브루드 커피', 
            'description': '더 사랑하자', 
            'products': [{
                'id': 2, 
                'isnew': False, 
                'isseason': False, 
                'title': '아이스 커피', 
                'image': 'drink_image_url', 
                'size': 'Tall(톨)', 
                'kcal': 100, 
                'sodium': 150, 
                'saturation': 200, 
                'sugar': 250, 
                'protein': 300, 
                'caffeine': 350
                }
            ]
        }
    }
)

    def test_product_list_get_filter_success(self):
        name = "콜드브루"
        response = self.client.get(f'/product?name={name}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),  {
        'results': [
            {
            'subcategory_id': 1, 
            'name': '콜드브루', 
            'description': '우리 사랑하자', 
            'products': [{
                'id'   : 1, 
                'isnew'   : True, 
                'isseason': False, 
                'title': '나이트로 바닐라 크림', 
                'image': 'drink_image_url', 
                'size': 'Tall(톨)', 
                'kcal': 10, 
                'sodium': 15, 
                'saturation': 20, 
                'sugar': 25, 
                'protein': 30, 
                'caffeine': 35
                }
            ]   
        }
    ]
}
)

class ProductDetailTest(TestCase):
    def setUpTestData():
        main_category = MainCategory.objects.create(name="음료")
        sub_category  = SubCategory.objects.create(name="콜드 브루", description="디카페인 에스프레소 샷 추가 기능", main_category=main_category)
        drink_status  = DrinkStatus.objects.create(name='강달쌘')

        drink = Drink.objects.create(
            id               = 1,
            sub_category     = sub_category,
            korean_name      = "아이스 커피",
            english_name     = "Iced Coffee",
            main_description = "깔끔하고 상큼함이 특징인 시원한 아이스 커피",
            sub_description  = "케냐, 하우스 블렌드 등 약간의 산미가 있는 커피를 드립 방식으로 추출한 후 얼음과 함께 제공하는 커피 입니다. 아이스 커피로 적합한 프리미엄 원두를 이용하여 깔끔하고 상큼한 맛을 느끼실 수 있습니다.",
            is_new           = True,
            is_season        = True,
            price            = 6000,
            density          = 20,
            taste            = 20,
            feel             = 20,
            drink_status     = drink_status
        )

        size = Size.objects.create(name='Tall')
        Nutrition.objects.create(
            drink      = drink, 
            size       = size, 
            kcal       = 1, 
            sodium     = 2, 
            saturation = 2, 
            sugar      = 10, 
            protein    = 5, 
            caffeine   = 5
        )

        
        Allergy.objects.bulk_create([
            Allergy(name = '콩'),
            Allergy(name = '두유'),
        ])

        DrinkAllergy.objects.bulk_create([
            DrinkAllergy(drink=drink, allergy=Allergy.objects.get(name='콩')),
            DrinkAllergy(drink=drink, allergy=Allergy.objects.get(name='두유'))
        ])

        for allergy_name in ['콩', '두유']:
            allergy = Allergy.objects.create(name = allergy_name)
            DrinkAllergy.objects.create(drink = drink, allergy = allergy)

    def setUp(self):
        pass
        
    def tearDown(self):
        Drink.objects.all().delete()

    def test_product_detail_veiw_success(self):
        response = client.get(reverse('detail', args=['1']))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_veiw_doesnotexist(self):
        response = client.get(reverse('detail', args=['10']))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error" : "DRINK_DOES_NOT_EXIST"})