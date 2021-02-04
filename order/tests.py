import json
import jwt

from my_settings import SECRET

from django.test    import Client, TestCase

from order.models   import Order, OrderStatus, Cart
from user.models    import User

from product.models import ( 
    Drink, 
    DrinkStatus, 
    MainCategory, 
    SubCategory, 
    Size
)

client = Client()

class CartViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
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
            drink_status     = drink_status,
            image_url        = "d"
        )
        user = User.objects.create(
            id      = 1,
            email   = 'jinukix@wecode.com',
            age     = '27',
            gender  = 'male'
        )

        token  = jwt.encode({"user_id":user.id}, key = SECRET, algorithm='HS256')
        cls.header = {"HTTP_Authorization" : token}

        size        = Size.objects.create(name='톨', id=1)
        orderstatus = OrderStatus.objects.create(status=False, id =2)
        order       = Order.objects.create(user = user, order_status = orderstatus)

        Cart.objects.create(drink=drink, order = order, size = size, quantity = 0)

    def test_get_cart_view_success(cls):
        
        product_list = [{
            "id"       : 1,
            'name'     : "아이스 커피",
            'img'      : "d",
            "cup_size" : "톨",
            'price'    : 6000,
            'amount'   : 0,
        }]

        response = client.get('/order/cart', **cls.header, content_type='application/json')
        cls.assertEqual(response.status_code, 200)
        cls.assertEqual({"item" : product_list}, response.json())

    def test_get_cart_view_tokenerror(cls):
        header = {"HTTP_Authorization" : '1234'}
        response = client.get('/order/cart', **header, content_type='application/json')
        cls.assertEqual(response.status_code, 401)
        cls.assertEqual({"message" : "Not Authorized"}, response.json())

    def test_post_cart_view_success(cls):
        data = {
            "size"  : 1,
            "drink" : 1,
            "amount": 1,
        }

        response = client.post('/order/cart', json.dumps(data), **cls.header, content_type='application/json')
        cls.assertEqual(response.status_code, 201)
        cls.assertEqual({"results" : "SUCCESS"}, response.json())

    def test_post_cart_view_keyerror(cls):
        data = {
            "size"  : 1,
            "key"   : 1,
        }

        response = client.post('/order/cart', json.dumps(data), **cls.header, content_type='application/json')
        cls.assertEqual(response.status_code, 400)
        cls.assertEqual({"error" : "KEY_ERROR"}, response.json())

    def test_patch_cart_view_success(cls):
        data = {
            "amount"  : 123,
            "drink"   : 1,
        }
        response = client.patch('/order/cart', json.dumps(data), **cls.header, content_type='application/json')
        cls.assertEqual(response.status_code, 200)
        cls.assertEqual({"results" : "SUCCESS"}, response.json())

    def test_patch_cart_view_doesnotexists(cls):
        data = {
            "amount"  : 123,
            "drink"   : 123,
        }
        response = client.patch('/order/cart', json.dumps(data), **cls.header, content_type='application/json')
        cls.assertEqual(response.status_code, 400)
        cls.assertEqual({"error" : "CART_DOES_NOT_EXISTS"}, response.json())

    def test_patch_cart_view_keyerror(cls):
        data = {
            "amount"  : 123,
            "key"     : 123,
        }
        response = client.patch('/order/cart', json.dumps(data), **cls.header, content_type='application/json')
        cls.assertEqual(response.status_code, 400) 
        cls.assertEqual({"error" : "KEY_ERROR"}, response.json())
