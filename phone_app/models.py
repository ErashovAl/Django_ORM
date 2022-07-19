from django.db import models

class Phone(models.Model):

    name = models.CharField(max_length=50, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    image = models.URLField(verbose_name='Картинка')
    release_date = models.DateTimeField(verbose_name='Дата выпуска')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.SlugField(max_length=255, verbose_name='URL')