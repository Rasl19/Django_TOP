from django.db import models


class RestaurantModels(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название ресторана')
    specialization = models.CharField(max_length=100, verbose_name='Тип кухни')
    address = models.CharField(max_length=100, unique=True, verbose_name='Адрес')
    web_site = models.URLField(unique=True, verbose_name='Web адресс')
    phone = models.CharField(max_length=5, unique=True, verbose_name='Телефон')

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.specialization = self.specialization.capitalize()
        self.address = self.address.title()
        super(RestaurantModels, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} | {self.address} | {self.phone}'
