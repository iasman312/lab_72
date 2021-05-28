from django.db import models

CHOICES = (("Moderated", "Модерированная"),
           ("New", "Новая")
)


class Quote:
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name='Автор')
    email = models.EmailField(null=False, blank=False, verbose_name="Email")
    rating = models.IntegerField(null=False, blank=False, verbose_name="Общий рейтинг")
    status = models.CharField(choices=CHOICES, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'quotes'
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

    def __str__(self):
        return self.text


class Rating:
    quote = models.ForeignKey(Quote, on_delete="CASCADE")
    rating = models.IntegerField(null=False, blank=False, verbose_name="Рейтинг")

    class Meta:
        db_table = 'ratings'
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return self.rating

