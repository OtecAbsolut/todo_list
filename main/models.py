from django.db import models


class ListModel(models.Model):
    """ Модель списка дел """
    name = models.CharField(max_length=128, verbose_name='Название списка')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}: {self.name} : {self.user}'

    class Meta:
        verbose_name = 'Список дел'
        unique_together = ('name', 'user')
