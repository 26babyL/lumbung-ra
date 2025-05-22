from django.shortcuts import render

# Create your views here.
def dashboard_view(request):
    return render(request, 'dashboard.html')
def products_view(request): 
    return render(request, 'products.html')
def add_product_view(request): 
    return render(request, 'add_product.html')
def categories_view(request): 
    return render(request, 'categories.html')
def inventory_view(request): 
    return render(request, 'inventory.html')
def sales_view(request): 
    return render(request, 'sales.html')
def transfers_view(request): 
    return render(request, 'transfers.html')
def reports_view(request): 
    return render(request, 'reports.html')
def team_view(request): 
    return render(request, 'team.html')
def settings_view(request): 
    return render(request, 'settings.html')
