from django.contrib import admin
from . models import Produktas, Customer, Cart

# Register your models here.

@admin.register(Produktas)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','pavadinimas','kaina_su_nuolaida','kategorija','nuotrauka']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'vartotojas', 'salis', 'miestas', 'zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'produktas', 'quantity']