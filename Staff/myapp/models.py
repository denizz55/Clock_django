from django.db import models

class Task(models.Model):
    name = models.CharField('Название', max_length=100)
    price = models.IntegerField('Цена', max_length=100)
    place = models.IntegerField('Количество', default=1)
    square = models.CharField('Адрес заказа', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'
