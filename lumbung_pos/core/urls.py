from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('products/', views.products_view, name='products'),
    path('products/add/', views.add_product_view, name='add_product'),
    path('categories/', views.categories_view, name='categories'),
    path('inventory/', views.inventory_view, name='inventory'),
    path('sales/', views.sales_view, name='sales'),
    path('transfers/', views.transfers_view, name='transfers'),
    path('reports/', views.reports_view, name='reports'),
    path('team/', views.team_view, name='team'),
    path('settings/', views.settings_view, name='settings'),
]
