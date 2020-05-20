import pytest
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.common.by import By
from django.db import connections
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

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
