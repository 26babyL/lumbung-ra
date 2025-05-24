from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

class InventoryItem(models.Model):
    product_title = models.CharField(max_length=200)          # Judul Produk
    variant_name = models.CharField(max_length=150, blank=True, null=True)  # Nama Varian
    store_name = models.CharField(max_length=150)              # Toko
    product_type = models.CharField(max_length=100)            # Tipe Produk
    sku = models.CharField(max_length=50)         # Nomor SKU
    price = models.DecimalField(max_digits=12, decimal_places=0)  # Harga
    barcode = models.CharField(max_length=100, blank=True, null=True)  # Barcode
    stock_units = models.IntegerField()                # Unit dalam Persediaan

    def __str__(self):
        return f"{self.product_title} ({self.store_name})"