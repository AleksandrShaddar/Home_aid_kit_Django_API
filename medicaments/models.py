from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Medicament(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    quantity = models.IntegerField(verbose_name='Количество')
    expiration_date = models.DateField(verbose_name='Срок годности')
    instruction = models.TextField(verbose_name='Инструкция')
    type_medicament = models.CharField(max_length=100, verbose_name='Тип')
    category_medicament = models.TextField(verbose_name='Категория')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Принадлежит')

    class Meta:
        ordering = ('name',)
