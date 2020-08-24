from django.db import models
from django.urls import reverse

STATUS_CHOICES = (
    ('a', 15),
    ('b', 20),
    ('c', 25),
	('d', 30),
	('e', 35),
	('f', 40),
	('g', 45),
)


class Category(models.Model):
    name = models.CharField("kategori adı", max_length=150, db_index=True)
    slug = models.SlugField("internet adresi",max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name = "kategori")
    name = models.CharField("ürün adı", max_length=100, db_index=True)
    slug = models.SlugField("internet adresi",max_length=100, db_index=True)
    description = models.TextField("Ürün açıklaması", blank=True)
    price = models.DecimalField("fiyat", max_digits=10, decimal_places=2)
    available = models.BooleanField("mevcut mu?", default=True)
    ogrenci_sayisi = models.CharField(max_length=1, choices=STATUS_CHOICES)
    stock = models.PositiveIntegerField("stok miktarı",default = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField("resim", upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('ogrenci_sayisi', )
        index_together = (('id', 'slug'),)
        verbose_name = 'Ürün'
        verbose_name_plural = "Ürünler"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
