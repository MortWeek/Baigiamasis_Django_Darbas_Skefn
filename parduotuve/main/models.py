from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SALIS_CHOICES=(
    ('Lietuva','Lietuva'),
    ('Latvia','Latvia'),
    ('Estonia','Estonia'),
)

CATEGORY_CHOICES=(
    ('M','Medziaga'),
    ('O','Oda'),
    ('U','Universalus'),
    ('R','Rinkiniai'),
    ('SE','Sepeciai'),
)

class Produktas(models.Model):
    pavadinimas = models.CharField(max_length=100)
    kaina = models.FloatField()
    kaina_su_nuolaida = models.FloatField()
    aprasymas = models.TextField()
    kategorija = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    nuotrauka = models.ImageField(upload_to='product')
    def __str__(self):
        return self.pavadinimas

class Customer(models.Model):
    vartotojas = models.ForeignKey(User, on_delete=models.CASCADE)
    vardas = models.CharField(max_length=200)
    pavarde = models.CharField(max_length=200)
    salis = models.CharField(choices=SALIS_CHOICES, max_length=100)
    miestas = models.CharField(max_length=50)
    telefonas = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    def __str__(self):
        return self.vardas

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    produktas = models.ForeignKey(Produktas,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    @property
    def total_cost(self):
        return self.quantity * self.produktas.kaina_su_nuolaida
