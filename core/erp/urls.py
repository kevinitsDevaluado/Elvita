from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.client.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.product.views import *
from core.erp.views.sale.views import *
from core.erp.views.Suppliers.views import *
from core.erp.views.RawMaterial.views import *
from core.erp.views.tests.views import TestView

app_name = 'erp'

urlpatterns = [
    # category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    # client
    path('client/list/', ClientListView.as_view(), name='client_list'),
    path('client/add/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    # product
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # test
    path('test/', TestView.as_view(), name='test'),
    # sale
    path('sale/list/', SaleListView.as_view(), name='sale_list'),
    path('sale/add/', SaleCreateView.as_view(), name='sale_create'),
    path('sale/delete/<int:pk>/', SaleDeleteView.as_view(), name='sale_delete'),
    path('sale/update/<int:pk>/', SaleUpdateView.as_view(), name='sale_update'),
    path('sale/invoice/pdf/<int:pk>/', SaleInvoicePdfView.as_view(), name='sale_invoice_pdf'),
    # Suppliers
    path('suppliers/list/', SuppliersListView.as_view(), name='suppliers_list'),
    path('suppliers/add/', SuppliersCreateView.as_view(), name='suppliers_create'),
    path('suppliers/delete/<int:pk>/', SuppliersDeleteView.as_view(), name='suppliers_delete'),
    path('suppliers/update/<int:pk>/', SuppliersUpdateView.as_view(), name='suppliers_update'),
    #path('sale/invoice/pdf/<int:pk>/', SaleInvoicePdfView.as_view(), name='sale_invoice_pdf'),
    #RawMaterial
    path('rawmaterial/list/', RawMaterialListView.as_view(), name='rawmaterial_list'),
    path('rawmaterial/add/', RawMaterialCreateView.as_view(), name='rawmaterial_create'),
    path('rawmaterial/delete/<int:pk>/', RawMaterialDeleteView.as_view(), name='rawmaterial_delete'),
    path('rawmaterial/update/<int:pk>/', RawMaterialUpdateView.as_view(), name='rawmaterial_update'),
    
]
