from django.db import models

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [('other', 'Разное'), ('TVs', 'Телевизоры'), ('notebooks', 'Ноутбуки')]
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    category = models.CharField(max_length=11, choices=CATEGORY_CHOICES, default='other', verbose_name='Категория')
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Описание')
    picture = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Картинка')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'