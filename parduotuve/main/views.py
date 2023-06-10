from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Cart, Produktas, Customer
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,"main/home.html")

def apie(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request,"main/apie.html", locals())

def kontaktai(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request,"main/kontaktai.html", locals())

class CategoryView(View):
    def get(self,request,val):
        produktas = Produktas.objects.filter(kategorija=val)
        pavadinimas = Produktas.objects.filter(kategorija=val).values('pavadinimas')
        return render(request,"main/kategorija.html",locals())

class CategoryTitle(View):
    def get(self,request,val):
        produktas = Produktas.objects.filter(pavadinimas=val)
        pavadinimas = Produktas.objects.filter(kategorija=produktas[0].kategorija).values('pavadinimas')
        return render(request,"main/kategorija.html",locals())

class ProductDetail(View):
    def get(self,request,pk):
        produktas = Produktas.objects.get(pk=pk)
        return render(request, "main/productdetail.html", locals())

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'main/customerregistration.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sveikiname! Vartotojo registracija sėkminga!")
        else:
            messages.warning(request, "Klaida! Netinkamai įvesti duomenys.")
        return render(request, 'main/customerregistration.html', locals())

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'main/profile.html', locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            vartotojas = request.user
            vardas = form.cleaned_data['vardas']
            pavarde = form.cleaned_data['pavarde']
            salis = form.cleaned_data['salis']
            miestas = form.cleaned_data['miestas']
            telefonas = form.cleaned_data['telefonas']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(vartotojas=vartotojas,vardas=vardas,pavarde=pavarde,salis=salis,miestas=miestas,telefonas=telefonas,zipcode=zipcode)
            reg.save()
            messages.success(request, "Išsaugojote profilio duomenys!")
        else:
            messages.warning(request,"Nepavyko išsaugoti duomenu!")
        return render(request, 'main/profile.html', locals())

def address(request):
    add = Customer.objects.filter(vartotojas=request.user)
    return render(request, 'main/address.html', locals())

class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request, 'main/updateAddress.html', locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.vardas = form.cleaned_data['vardas']
            add.pavarde = form.cleaned_data['pavarde']
            add.salis = form.cleaned_data['salis']
            add.miestas = form.cleaned_data['miestas']
            add.telefonas = form.cleaned_data['telefonas']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Profilio duomenys atnaujinti!")
        else:
            messages.warning(request, "Nepavyko atnaujinti duomenu!")
        return redirect("address")

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.produktas.kaina_su_nuolaida
        amount = amount + value
    totalamount = amount + 10
    return render(request, 'main/addtocart.html',locals())

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    produktas = Produktas.objects.get(id=product_id)
    Cart(user=user, produktas=produktas).save()
    return redirect("/cart")

class checkout(View):
    def get(self,request):
        vartotojas = request.user
        add = Customer.objects.filter(vartotojas=vartotojas)
        cart_items = Cart.objects.filter(user=vartotojas)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.produktas.kaina_su_nuolaida
            famount = famount + value
        totalamount = famount + 40
        return render(request, 'main/checkout.html', locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(produktas=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.produktas.kaina_su_nuolaida
            amount = amount + value
        totalamount = amount + 10
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(produktas=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.produktas.kaina_su_nuolaida
            amount = amount + value
        totalamount = amount + 10
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(produktas=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.produktas.kaina_su_nuolaida
            amount = amount + value
        totalamount = amount + 10
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)

