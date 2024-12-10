from django.db import models


class PhoneBook(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    email = models.EmailField(max_length=128, verbose_name='Email', unique=True)
    phone = models.CharField(max_length=11, verbose_name='Телефон', default=7, unique=True)
    note = models.TextField(max_length=100, blank=True, null=True, verbose_name='Примечание')

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        super(PhoneBook, self).save(*args, **kwargs)

    def __str__(self):
        return f'Имя: {self.first_name} | Фамилия: {self.last_name} | Телефон: {self.phone}'
