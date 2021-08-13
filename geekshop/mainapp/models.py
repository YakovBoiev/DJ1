from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=64,
        unique=True, )
    description = models.TextField(
        verbose_name='описание',
        blank=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        verbose_name='категория',
        on_delete=models.CASCADE)
    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128)
    image = models.ImageField(
        upload_to='products_images',
        blank=True)
    short_desc = models.CharField(
        verbose_name='краткое описание продукта',
        max_length=60,
        blank=True)
    descriptions = models.TextField(
        verbose_name='описание продукта',
        blank=True)
    price = models.DecimalField(
        verbose_name='цена продукта',
        max_digits=8,
        decimal_places=2, default=0)
    quanaty = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0)

    is_active = models.BooleanField(
        verbose_name='активный',
        default=True
    )

    def __str__(self):
        return f"{self.name} {self.pk}"

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
