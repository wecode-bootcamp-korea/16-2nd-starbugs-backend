<<<<<<< HEAD
=======
import json
import jwt
import bcrypt

from django.db      import connection
from django.test    import Client
from django.test    import TestCase

from my_settings    import SECRET, ALGORITHM

from user.models    import User
from order.models   import *
from product.models import *

class CartTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        cls.drink_status = DrinkStatus.objects.create(
            name="강달쎈"
        )

        cls.user = User.objects.create(
            id     = 1,
            gender = "남자", 
            age = "20대", 
            email = "1004kjs_@nave.com", 
            density = 30, 
            feel = 70, 
            taste = 25, 
        )

        cls.order_status = OrderStatus.objects.create(
            status = False
        )

        cls.order = Order.objects.create(
            user = cls.user, 
            order_status = cls.order_status
        )

        cls.category = MainCategory.objects.create(
            name="음료"
        )

        cls.subcategory = SubCategory.objects.create(
            name = "콜드브루", 
            description = "우리 사랑하자", 
            main_category = cls.category
        )

        cls.size_1      = Size.objects.create(name="Tall(톨)")
        cls.size_2      = Size.objects.create(name="regular(레귤러)") 
            
        cls.nitro = Drink.objects.create(
            sub_category = cls.subcategory,
            korean_name  = "나이트로 바닐라 크림",
            english_name = "Nitro Vanilla Cream",
            main_description = "사랑해",
            sub_description = "더 사랑해",
            is_new       = True,
            is_season    = False,
            density      = 30,
            taste        = 70,
            feel         = 25,
            price        = 1000,
            image_url    = 'drink_image_url',
            drink_status = cls.drink_status
            )

        cls.cart = Cart.objects.create(
            drink    = cls.nitro,
            size     = cls.size_2,
            order    = cls.order,
            quantity = 5
            )

        cls.token = jwt.encode({'user_id' : User.objects.get(id=1).id}, SECRET, algorithm = ALGORITHM)

    def tearDown(self):
        DrinkStatus.objects.all().delete()
        Cart.objects.all().delete()
        Drink.objects.all().delete()
        Order.objects.all().delete()
        OrderStatus.objects.all().delete()
        SubCategory.objects.all().delete()
        MainCategory.objects.all().delete()
        User.objects.all().delete()

    def test_cart_create_or_update(self):
        client = Client()
        headers = {"HTTP_Authorization" : self.token}
        token = headers["HTTP_Authorization"]
        payload  = jwt.decode(token, SECRET, algorithms = ALGORITHM)
        user     = User.objects.get(id = payload['user_id'])
        data = {
            'drink' : self.nitro.id,
            'size'  : self.size_1.id
        }
        response = client.post('/cart', json.dumps(data), content_type = 'application/json', **headers)
        self.assertEqual(response.status_code, 201)

    def test_cart_create_or_update_key_error(self):
        client = Client()
        headers = {"HTTP_Authorization" : self.token}
        token = headers["HTTP_Authorization"]
        payload  = jwt.decode(token, SECRET, algorithms = ALGORITHM)
        user     = User.objects.get(id = payload['user_id'])
        data = {
            'size'  : self.size_1.id
        }
        response = client.post('/cart', json.dumps(data), content_type = 'application/json', **headers)
        self.assertEqual(response.status_code, 400)

    def test_cart_create_or_update_key_error(self):
        client = Client()
        headers = {"HTTP_Authorization" : self.token}
        token = headers["HTTP_Authorization"]
        payload  = jwt.decode(token, SECRET, algorithms = ALGORITHM)
        user     = User.objects.get(id = payload['user_id'])
        data = {
            'drink' : self.nitro.id
        }
        response = client.post('/cart', json.dumps(data), content_type = 'application/json', **headers)
        self.assertEqual(response.status_code, 400)

    def test_cart_patch_quality_check(self):
        client   = Client()
        headers  = {"HTTP_Authorization" : self.token}
        token    = headers["HTTP_Authorization"]
        payload  = jwt.decode(token, SECRET, algorithms = ALGORITHM)
        user     = User.objects.get(id = payload['user_id'])
        data = {
            'id'       : self.nitro.id,
            'amount'   : 5
        }
        response = client.patch('/cart', json.dumps(data), content_type = 'application/json', **headers)
        self.assertEqual(response.status_code, 201)

    def test_cart_patch_not_quality_check(self):
        client   = Client()
        headers  = {"HTTP_Authorization" : self.token}
        token    = headers["HTTP_Authorization"]
        payload  = jwt.decode(token, SECRET, algorithms = ALGORITHM)
        user     = User.objects.get(id = payload['user_id'])
        data = {
            'id'       : self.nitro.id
        }
        response = client.patch('/cart', json.dumps(data), content_type = 'application/json', **headers)
        self.assertEqual(response.status_code, 201)

    def test_cart_quantity_key_error(self):
        client   = Client()
        headers  = {"HTTP_Authorization" : self.token}
        token    = headers["HTTP_Authorization"]
        payload  = jwt.decode(token, SECRET, algorithms = ALGORITHM)
        user     = User.objects.get(id = payload['user_id'])
        data = {
            'amount'   : 5
        }
        response = client.patch('/cart', json.dumps(data), content_type = 'application/json', **headers)
        self.assertEqual(response.status_code, 400)

    def test_cart_get_success(self):
        client   = Client()
        headers  = {"HTTP_Authorization" : self.token}
        token    = headers["HTTP_Authorization"]
        payload  = jwt.decode(token, SECRET, algorithms = ALGORITHM)
        user     = User.objects.get(id = payload['user_id'])
        response = client.get('/cart', content_type = 'application/json', **headers)
        self.assertEqual(response.status_code, 200)
>>>>>>> b0d300c (장바구니 생성)
