import json

from django.views   import View
from django.http    import JsonResponse

from order.models   import Cart, Order, OrderStatus
from user.models    import User
from product.models import Size

from user.utils     import check_user

class ShoppingBasket(View):
    @check_user
    def get(self, request):
        user_id   = 1 
        order     = Order.objects.prefetch_related('carts')[0]

        if not Order.objects.filter(user_id=user_id).exists():
            return JsonResponse({"results" : "장바구니에 상품이 없습니다."}, status = 400)

        product_list = [
            {
                'id'          : cart.drink.id,
                'name'        : cart.drink.korean_name,
                'img'         : cart.drink.image_url,
                "cup_size"    : cart.size.name,
                'amount'      : cart.quantity,
                'price'       : int(cart.drink.price),
            }
        for cart in order.carts.all()]
        return JsonResponse({"item" : product_list}, status = 200)

    @check_user
    def post(self, request):
        try:
            user_id  = 1
            data     = json.loads(request.body)
            drink_id = data['drink']
            size_id  = data['size']
        
            if not Order.objects.filter(user_id = user_id).exists():
                Order.objects.create(user_id = user_id, order_status_id=2)

            order    = Order.objects.get(user_id = user_id)
            if Cart.objects.filter(drink_id = drink_id, size_id = size_id, order = order).exists():
                quantity = Cart.objects.filter(drink_id = drink_id, size_id = size_id, order = order)[0].quantity
                Cart.objects.filter(drink_id = drink_id, size_id = size_id, order = order).update(quantity=quantity+1)

                return JsonResponse({"results" : "SUCCESS"}, status=201)

            Cart.objects.create(drink_id = drink_id, size_id = size_id, order = order, quantity=1)
            
            return JsonResponse({"results" : "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"results" : "KEY ERROR"}, status=400)
  
    @check_user       
    def patch(self, request):
        try:
            user_id   = 1
            data      = json.loads(request.body)
            drink_id  = data['id']
            quantity  = data.get('amount')
            order     = Order.objects.get(user_id = user_id)
      
            if quantity:
              Cart.objects.filter(drink_id = drink_id).update(quantity=quantity)
            Order.objects.filter(user_id = user_id).update(order_status = 1)
            return JsonResponse({"results" : "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"results" : "KEYERROR"}, status=400)