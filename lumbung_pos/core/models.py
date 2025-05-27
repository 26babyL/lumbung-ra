from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    sku = models.CharField("SKU", max_length=100, unique=True)
    name = models.CharField("Product Name", max_length=200)
    description = models.TextField("Description", blank=True)

    barcode = models.CharField("Barcode", max_length=100, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)
    product_type = models.CharField("Product Type", max_length=100, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    option1_name = models.CharField("Option 1 Name", max_length=100, blank=True)
    option1_value = models.CharField("Option 1 Value", max_length=100, blank=True)
    option2_name = models.CharField("Option 2 Name", max_length=100, blank=True)
    option2_value = models.CharField("Option 2 Value", max_length=100, blank=True)

    buying_price = models.IntegerField("Buying Price", null=True, blank=True)
    selling_price = models.IntegerField("Selling Price", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sku} - {self.name}"

    class Meta:
        db_table = 'database_allproducts'
