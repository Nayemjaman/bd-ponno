from decimal import Decimal

from djongo import models

# Create your models here.
# https://github.com/nesdis/djongo/pull/525/commits/86dbe3918ac4b2299d6aa3249a4509996f53920c

# add this code segment in  the djongo/operations.py file  and convert it to use DecimalField
# def adapt_decimalfield_value(self, value, max_digits=None, decimal_places=None):
#     if value is None:
#         return None
#     return bson.Decimal128(super().adapt_decimalfield_value(value, max_digits, decimal_places))


from products.fields import MongoDecimalField


class Product(models.Model):
    vendor = models.CharField(max_length=100, blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    product_url = models.CharField(max_length=255, blank=False, null=False)
    price = MongoDecimalField(max_length=10, decimal_places=2, blank=True, null=True, max_digits=10,
                              default=Decimal(0.0))
    image_url = models.CharField(max_length=255, blank=True, null=True)
    in_stock = models.BooleanField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "product"
        verbose_name_plural = 'products'
        indexes = [
            models.Index(fields=['name'], name='%(app_label)s_%(class)s_name_index'),
        ]

    def __str__(self):
        return self.name
