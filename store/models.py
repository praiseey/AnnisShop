from django.db import models
from django.urls import reverse


class Categories(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    # def get_absolute_url(self):
    #     return reverse('store:store_list')

    def __str__(self):
        return self.category_name

    @property
    def get_products(self):
        return Product.objects.filter(category=self.name)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField(default=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=2083, default=True)
    size = models.PositiveSmallIntegerField()
    colour = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

