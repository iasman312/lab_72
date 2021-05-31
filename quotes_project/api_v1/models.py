from django.db import models

CHOICES = (("Moderated", "Модерированная"),
           ("New", "Новая")
)


class Quote(models.Model):
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name='Автор')
    email = models.EmailField(null=False, blank=False, verbose_name="Email")
    rating = models.IntegerField(verbose_name="Общий рейтинг", default=0)
    status = models.CharField(max_length=200, choices=CHOICES, verbose_name='Статус', default="New")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'quotes'
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'
        permissions = [('view_all', 'View all')]


class Rating(models.Model):
    quote = models.ForeignKey(
           'api_v1.Quote',
           on_delete=models.CASCADE,
           related_name='ratings',
           verbose_name='Цитата',
           null=False,
           blank=False
    )
    rating = models.IntegerField(null=False, blank=False, verbose_name="Рейтинг")
    session = models.CharField(max_length=200, verbose_name="Сессия", blank=True, null=True)

    class Meta:
        db_table = 'ratings'
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


