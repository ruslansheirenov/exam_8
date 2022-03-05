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


class Review(models.Model):
    RAITING_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    content = models.TextField(max_length=2000, verbose_name="Контент")
    product = models.ForeignKey("webapp.Product", on_delete=models.CASCADE, related_name="reviews", verbose_name="Продукт",)
    rating = models.IntegerField(choices=RAITING_CHOICES)
    check_moder = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'