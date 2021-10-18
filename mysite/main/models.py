from django.db import models


class Names(models.Model):
    objects = None
    name = models.CharField("Имя", max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'office{self.id}'

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'
