from main.forms import ListForm
from main.models import ListModel
import pytest


@pytest.mark.django_db
def test_invalid_token_fields(new_client):
    data = {
        'name': 'Тестовый список',
        'user': new_client
    }
    form = ListForm(data)
    form.save()
    form = ListForm(data)
    assert 'Имя уже существует' in form.non_field_errors()
