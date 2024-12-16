from django.db import models


class BuyerModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    phone = models.CharField(max_length=11, default=7, unique=True, verbose_name='Телефон')
    email = models.EmailField(unique=True, verbose_name='Email')

    def __str__(self):
        return f'{self.name} {self.surname}'


class SalesmanModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    phone = models.CharField(max_length=11, default=7, unique=True, verbose_name='Телефон')
    email = models.EmailField(unique=True, verbose_name='Email')
    hiring_date = models.DateField(verbose_name='Дата трудоустройства')
    job_position = models.CharField(choices=(
        ('sal_man', 'Продавец'), ('sen_sal_man', 'Старший продавец'), ('head_sal_dep', 'Руководитель отдела продаж')),
        max_length=30, verbose_name='Должность')

    def __str__(self):
        return f'{self.name} {self.surname}'


class ProductModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена $')
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'


class SalesInfoModel(models.Model):
    buyer = models.ForeignKey(BuyerModel, on_delete=models.CASCADE, verbose_name='Покупатель')
    salesman = models.ForeignKey(SalesmanModel, on_delete=models.CASCADE, verbose_name='Продавец')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='Продукт')
    date_sales = models.DateField(verbose_name='Дата продажи')
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество')
    sum_sales = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, *args, **kwargs):
        self.sum_sales = self.product.price * self.quantity
        super(SalesInfoModel, self).save(*args, **kwargs)

    def __str__(self):
        return f'Покупатель: {self.buyer.name} | Продавец: {self.salesman.name} | Сумма: {self.sum_sales}'
