# import_inventory.py
import pandas as pd
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumbung_pos.settings')
django.setup()

from core.models import InventoryItem

# Ganti path file Excel kamu
df = pd.read_excel('data_inventory.xlsx')

for idx, row in df.iterrows():
    try:
        InventoryItem.objects.create(
            product_title = row['Judul Produk'],
            variant_name = row.get('Nama Varian', ''),
            store_name = row['Toko'],
            product_type = row['Tipe Produk'],
            sku = row['Nomor SKU'],
            price = row['Harga'],
            barcode = row.get('Barcode', ''),
            stock_units = row['Unit dalam Persediaan']
        )
    except Exception as e:
        print(f"❌ Error di baris {idx+2}: {e}")

print("✅ Import selesai.")
