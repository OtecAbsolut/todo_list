from django.test import Client
from django.shortcuts import reverse
import pytest
from main.forms import ListForm

TEST_CLIENT = {
    'username': 'TestUser',
    'email': '123@123.ru',
    'password': 'q1w2e3r4TT',
}


def test_item_page_return_correct_htm(client, new_client, new_list):
    """
    Проверка что рендерится правильный шаблон элементов списка
    """
    client.login(username=new_client.username, password=TEST_CLIENT['password'])
    response = client.get(
        reverse('list_item:list_item', kwargs={'pk': new_list.id})
    )
    html = response.content.decode('utf8')
    assert response.status_code == 200
    assert '<title>Дела</title>' in html
    assert new_list.name in html
    assert 'list.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_save_new_list_item(new_client, new_list):
    """
    Проверка вьюхи создание нового списка дел
    """
    csrf_client = Client(enforce_csrf_checks=True)
    csrf_client.login(
        username=new_client.username, password=TEST_CLIENT['password']
    )
    csrf_client.get(reverse('list_item:create', kwargs={'pk': new_list.id}))
    csrf = csrf_client.cookies['csrftoken']
    response = csrf_client.post(
        reverse('list_item:create', kwargs={'pk': new_list.id}), data={
            'name': 'Какое то дело',
            'expire_date': '2020-05-25',
            'csrfmiddlewaretoken': csrf.value
        })
    assert response.status_code == 302, response.content.decode()

    response = csrf_client.get(
        reverse('list_item:list_item', kwargs={'pk': new_list.id})
    )
    html = response.content.decode('utf8')
    assert 'Какое то дело' in html
