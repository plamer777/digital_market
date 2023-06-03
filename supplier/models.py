"""This file contains different models for supplier application"""
from django.core.validators import MinValueValidator
from django.contrib.contenttypes.models import ContentType
from django.db import models
# ------------------------------------------------------------------------


class Product(models.Model):
    """This class represents a product spreadsheet in the database"""
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    model = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}, {self.model}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = "Товары"


class Contact(models.Model):
    """This class represents a contact spreadsheet in the database"""
    email = models.EmailField(max_length=50)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    home_number = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f'{self.email}, {self.country}'

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class BaseModel(models.Model):
    """This class is a base abstract model with fields common to all models"""
    contact = models.ManyToManyField(Contact)
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length=100)
    debt = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        contacts = ', '.join(str(item) for item in self.contact.all())
        products = ', '.join(str(item) for item in self.product.all())
        return f'{self.name}: ({contacts}), ({products})'

    class Meta:
        abstract = True


class Factory(BaseModel):
    """This class represents a factory spreadsheet in the database"""
    class Meta:
        verbose_name = "Фабрика"
        verbose_name_plural = "Фабрики"


class RetailNetwork(BaseModel):
    """This class represents a retail network spreadsheet in the database"""
    supplier = models.ForeignKey(
        Factory, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"


class IndividualEntrepreneur(BaseModel):
    """This class represents an individual entrepreneur spreadsheet in the
    database"""
    supplier = models.ForeignKey(
        RetailNetwork, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"
