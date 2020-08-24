from django.db import models
from shop.models import Product
from accounts.models import User


class Order(models.Model):
    first_name = models.CharField("Adınız", max_length=60)
    last_name = models.CharField("Soyadınız",max_length=60)
    email = models.EmailField()
    address = models.CharField("Adres", max_length=150)
    postal_code = models.CharField("Posta Kodu", max_length=30)
    city = models.CharField("Şehir", max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField("Ödeme tutarı", default=False)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Sipariş'
        verbose_name_plural = "Siparişler"
		

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name = "Sipariş")
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name = "Ürün")
    price = models.DecimalField("Fiyat", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Miktar", default=1)
    user = models.ForeignKey(User, related_name='kullanici', on_delete=models.CASCADE, verbose_name = "Kullanıcı")

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

