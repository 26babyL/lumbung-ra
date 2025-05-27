import pandas as pd
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumbung_pos.settings')
django.setup()

from core.models import Product, Vendor, Tag

df = pd.read_excel('products.xlsx')
print("Kolom ditemukan:", df.columns.tolist())

for idx, row in df.iterrows():
    try:
        sku = str(row['SKU']).strip()
        if Product.objects.filter(sku=sku).exists():
            continue

        vendor_name = str(row.get('Vendor', '')).strip()
        vendor, _ = Vendor.objects.get_or_create(name=vendor_name)

        # Tangani NaN pada harga
        buying_price = row.get('BuyingPrice', 0)
        if pd.isna(buying_price):
            buying_price = 0

        selling_price = row.get('Price', 0)
        if pd.isna(selling_price):
            selling_price = 0

        product = Product.objects.create(
            sku=sku,
            name=str(row['Name']).strip(),
            description=row.get('Description', ''),
            barcode=row.get('Barcode', ''),
            vendor=vendor,
            product_type=row.get('Product Type', ''),
            option1_name=row.get('Option 1 Name', ''),
            option1_value=row.get('Option 1 Value', ''),
            option2_name=row.get('Option 2 Name', ''),
            option2_value=row.get('Option 2 Value', ''),
            buying_price=int(buying_price),
            selling_price=int(selling_price),
        )

        tags_str = row.get('Tags', '')
        if pd.notna(tags_str) and tags_str:
            tag_names = [t.strip() for t in tags_str.split(',')]
            for tag_name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                product.tags.add(tag)

    except Exception as e:
        print(f"[X] Gagal impor baris {idx+2}: {e}")

print("✅ Import selesai.")
# Ensure the script is run in the Django environment
# This script imports products from an Excel file into the Django database.