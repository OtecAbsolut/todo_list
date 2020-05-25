import pytest
from django.contrib.auth.models import User
from main.models import ListModel


TEST_CLIENT = {
    'username': 'TestUser',
    'email': '123@123.ru',
    'password': 'q1w2e3r4TT',
}


@pytest.fixture
def new_client(db):
    new_client = User(
        username=TEST_CLIENT['username'],
        email=TEST_CLIENT['email'],
    )
    new_client.set_password(TEST_CLIENT['password'])
    new_client.save()
    return new_client


@pytest.fixture
def new_list(new_client):
    list_ = ListModel(
        name='Тестовый список дел',
        user=new_client
    )
    list_.save()
    return list_
