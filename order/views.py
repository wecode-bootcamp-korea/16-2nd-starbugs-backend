import json

from django.views       import View
from django.http        import JsonResponse

from order.models       import Cart, Order
from django.db.models   import F

from user.utils         import check_user

class CartView(View):
    @check_user
    def get(self, request):
        try:
            user     = request.user
            order, _ = Order.objects.get_or_create(user=user, order_status_id = 2)
            carts    = Cart.objects.filter(order = order)

            product_list = [{
                'cart_id'  : cart.id,
                'id'       : cart.drink.id,
                'name'     : cart.drink.korean_name,
                'img'      : cart.drink.image_url,
                "cup_size" : cart.size.name,
                'amount'   : cart.quantity,
                'price'    : int(cart.drink.price),
            } for cart in carts]

            return JsonResponse({"item" : product_list}, status = 200)
        except Order.DoesNotExist:
            return JsonResponse({"error" : "ORDER_DOES_NOT_EXISTS"}, status=400)

    @check_user
    def post(self, request):
        try:
            data     = json.loads(request.body)
            user     = request.user
            order, _ = Order.objects.get_or_create(user=user, order_status_id = 2)
            drink_id = data['drink']
            size_id  = data['size']
            amount   = data['amount']

            cart, _  = Cart.objects.get_or_create(
                drink_id = drink_id,
                size_id  = size_id,
                order    = order
            )

            cart.quantity = F('quantity') + amount
            cart.save()

            return JsonResponse({"results" : "SUCCESS"}, status=201)
            
        except Cart.DoesNotExist:
            return JsonResponse({"error" : "CART_DOES_NOT_EXISTS"}, status=400)
        except KeyError:
            return JsonResponse({"error" : "KEY_ERROR"}, status=400)
        except Order.DoesNotExist:
            return JsonResponse({"error" : "ORDER_DOES_NOT_EXISTS"}, status=400)
        
    @check_user       
    def patch(self, request):
        try:
            data  = json.loads(request.body)
            order = Order.objects.get(user=request.user, order_status_id = 2)
            cart  = Cart.objects.get(
                drink_id = data['drink'],
                order    = order,
                size_id  = data['size'],
            )
            cart.quantity = data['amount']
            cart.save()

            return JsonResponse({"results" : "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"error" : "KEY_ERROR"}, status=400) 
        except Order.DoesNotExist:
            return JsonResponse({"error" : "ORDER_DOES_NOT_EXISTS"}, status=400)
        except Cart.DoesNotExist:
            return JsonResponse({"error" : "CART_DOES_NOT_EXISTS"}, status=400)