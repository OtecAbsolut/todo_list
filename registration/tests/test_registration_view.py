from django.test import Client
import pytest
from django.shortcuts import reverse
from django.contrib.auth.models import User


def test_login_page_return_correct_html(client):
    """
    Проверка что рендерится правильный шаблон
    страницы ввода логина и пароля
    """
    response = client.get(reverse('registration:login'))
    html = response.content.decode('utf8')
    assert response.status_code == 200
    assert html.startswith('<!DOCTYPE html>')
    assert '<title>Войти</title>' in html
    assert html.strip().endswith('</html>')
    assert 'login.html' in [t.name for t in response.templates]


def test_registration_page_return_correct_htm(client):
    """
    Проверка что рендерится правильный шаблон
    страницы регистрации
    """
    response = client.get(reverse('registration:new_user'))
    html = response.content.decode('utf8')
    assert response.status_code == 200
    assert html.startswith('<!DOCTYPE html>')
    assert '<title>Регистрация</title>' in html
    assert html.strip().endswith('</html>')
    assert 'registration.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_can_save_a_post_request(client):
    """
    Создание нового пользователя
    """
    response = client.post(reverse('registration:new_user'), data={
        'username': 'test_user',
        'password1': '12345tQwe',
        'password2': '12345tQwe',
        'email': '123@123.ru',
    })
    assert response.status_code == 302
    user = User.objects.get(username='test_user')
    # Так лучше не делать
    assert user
    assert user.email == '123@123.ru'



