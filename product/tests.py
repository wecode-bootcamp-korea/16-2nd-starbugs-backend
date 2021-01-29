from django.test    import TestCase, Client
from product.models import ( 
    Allergy, 
    Drink, 
    DrinkAllergy, 
    MainCategory, 
    Size, 
    SubCategory, 
    Nutrition, 
)

from django.urls    import reverse

client = Client()

class ProductDetailTest(TestCase):
    def setUp(self):

        main_category = MainCategory.objects.create(name="음료")
        sub_category  = SubCategory.objects.create(name="콜드 브루", description="디카페인 에스프레소 샷 추가 기능", main_category=main_category)

        drink = Drink.objects.create(
            id               = 1,
            sub_category     = sub_category,
            korean_name      = "아이스 커피",
            english_name     = "Iced Coffee",
            main_description = "깔끔하고 상큼함이 특징인 시원한 아이스 커피",
            sub_description  = "케냐, 하우스 블렌드 등 약간의 산미가 있는 커피를 드립 방식으로 추출한 후 얼음과 함께 제공하는 커피 입니다. 아이스 커피로 적합한 프리미엄 원두를 이용하여 깔끔하고 상큼한 맛을 느끼실 수 있습니다.",
            destiny          = 100,
            is_new           = True,
            is_season        = True,
            price            = 6000,
            imgae_url        = 1,
            destiny          = 20,
            taste            = 20,
            feel             = 20
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

        for allergy_name in ['콩', '두유']:
            allergy = Allergy.objects.create(name = allergy_name)
            DrinkAllergy.objects.create(drink = drink, allergy = allergy)
        
    def tearDown(self):
        Drink.objects.all().delete()

    def test_product_detail_veiw_success(self):
        response = client.get(reverse('detail', args=['1']))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_veiw_doesnotexist(self):
        response = client.get(reverse('detail', args=['10']))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"MESSAGE":"Drink does not exist"})