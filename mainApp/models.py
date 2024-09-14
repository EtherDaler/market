from django.db import models
from datetime import datetime


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    date_of_create = models.DateTimeField(verbose_name='Дата и время создания')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_of_create = datetime.now()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товары'