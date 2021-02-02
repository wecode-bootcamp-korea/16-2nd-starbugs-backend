from django.db      import models

from user.models    import User

class Order(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at   = models.DateTimeField(auto_now_add=True)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE, related_name='orders') 

    class Meta:
        db_table = "orders"


class Cart(models.Model):
    drink    = models.ForeignKey("product.Drink", on_delete=models.CASCADE, related_name="carts")
    size     = models.ForeignKey("product.Size", on_delete=models.CASCADE)
    order    = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="carts")
    quantity = models.IntegerField()

    class Meta:
        db_table = "carts"
        


class OrderStatus(models.Model):
    status = models.BooleanField()

    class Meta:
        db_table = "orderstatus"