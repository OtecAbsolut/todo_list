from django.db import models


class ListItem(models.Model):
    """ Модель элемента списка """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    priority = models.SmallIntegerField(verbose_name='Приоритет', default=0)
    expire_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=128, verbose_name='Название')
    list = models.ForeignKey(
        'main.ListModel', on_delete=models.CASCADE, verbose_name='Список дел'
    )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        list_ = self.list
        # Если у всех элементов True, то True будет и у списка
        ListItem.objects.filter(list=list_)
        if all(list_.listitem_set.all().values_list('is_done', flat=True)):
            list_.is_done = True
            list_.save()
        else:
            # А если предположим что одно дело опять стало False, то
            # Надо сделать False и у списка (Если при это оно было True)
            if list_.is_done:
                list_.is_done = False
                list_.save()

    class Meta:
        verbose_name = 'Элемент списка'
        unique_together = ('name', 'list')
