from django.template.defaulttags import register
from todo_list_ngu.settings import DIV_COUNT


@register.filter
def get_count(lists):
    """
    Возвращает список - количество, для генераци пустых блоков
    """

    return list(range(DIV_COUNT - len(lists)))


