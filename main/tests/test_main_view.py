from django.test import Client
from django.shortcuts import reverse
import pytest
from main.forms import ListForm


TEST_CLIENT = {
    'username': 'TestUser',
    'email': '123@123.ru',
    'password': 'q1w2e3r4TT',
}


def test_main_page_redirect_if_non_auth(client):
    """ Проверка что происходит редирект если не авторизован """
    response = client.get('/')
    assert response.status_code == 302


def test_main_page_return_correct_htm(client, new_client):
    """
    Проверка что рендерится правильный шаблон главной страницы
    """
    client.login(username=new_client.username, password=TEST_CLIENT['password'])
    response = client.get(reverse('main:main'))
    html = response.content.decode('utf8')
    assert response.status_code == 200
    assert '<title>Главная</title>' in html
    assert html.strip().endswith('</html>')
    assert 'index.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_save_new_list_post_request_(client, new_client):
    """
    Проверка вьюхи создание нового списка дел
    """
    csrf_client = Client(enforce_csrf_checks=True)
    csrf_client.login(
        username=new_client.username, password=TEST_CLIENT['password']
    )
    csrf_client.get(reverse('main:create'))
    csrf = csrf_client.cookies['csrftoken']
    response = csrf_client.post(reverse('main:create'), data={
        'name': 'Тестовый список дел',
        'csrfmiddlewaretoken': csrf.value
    })
    assert response.status_code == 302, response.content.decode()

    response = csrf_client.get(reverse('main:main'))
    html = response.content.decode('utf8')
    assert 'Тестовый список дел' in html


