from django.db      import models

from user.models    import User

class Order(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "orders"

class Cart(models.Model):
    drink    = models.ForeignKey("Drink", on_delete=models.CASCADE, related_name="carts")
    size     = models.ForeignKey("Size", on_delete=models.CASCADE)
    order    = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="carts")
    quantity = models.IntegerField()

    class Meta:
        db_table = "carts"

class OrderStatus(models.Model):
    order  = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="order_statuses")
    status = models.BooleanField()

    class Meta:
        db_table = "orderstatuses"

