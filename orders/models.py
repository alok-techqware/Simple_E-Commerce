from django.db import models
from shop.models import Product

# from time import gmtime, strftime


class Order(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    city = models.CharField(max_length=60)
    street = models.CharField(max_length=60)
    house_number = models.CharField(max_length=10)
    apartment_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    # delivery = models.DateTimeField(auto)

    #  showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return "Order {}".format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "{}".format(self.id)

    def get_cost(self):
        return self.price * self.quantity
