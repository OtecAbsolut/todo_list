import pytest
from list_item.models import ListItem


@pytest.mark.django_db
def test_save_method(new_list):
    """ Тест метода save в модели ListItem """
    list_item = ListItem.objects.create(
        name='Какое то дело',
        list=new_list
    )
    assert new_list.is_done is False
    list_item.is_done = True
    list_item.save()
    assert new_list.is_done
    list_item.is_done = False
    list_item.save()
    assert new_list.is_done is False
