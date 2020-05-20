from main.forms import ListForm
from main.models import ListModel
import pytest


@pytest.mark.django_db
def test_invalid_token_fields(new_client):
    ListForm({
        'name': 'Тестовый список',
        'user': new_client
    }).save()

    assert 'Имя уже существует' in ListForm(
        {'name': 'Тестовый список', 'user': new_client}).non_field_errors()
