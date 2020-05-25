from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
import time


TEST_CLIENT = {
    'username': 'TestUser',
    'email': '123@123.ru',
    'password': 'q1w2e3r4TT',
}


def test_open_login_page(client, live_server, new_client):
    """
    Новый пользователь Юля, открывает
    браузер и решает ввести 'http://127.0.0.1:8000/'.
    Попадает на страницу с title 'Войти' и надписью ВХОД
    Вводит тестовый логин и пароль и переходит на главную
    """
    browser = webdriver.Firefox(
        executable_path='C:\\todo_list_ngu\\todo_list_ngu\geckodriver.exe')
    browser.get(live_server.url)
    assert browser.title == 'Войти'
    login = browser.find_element_by_name('login')
    password = browser.find_element_by_name('password')
    login.send_keys(TEST_CLIENT['username'])
    password.send_keys(TEST_CLIENT['password'])

    button = browser.find_element_by_id('login-submit-btn')
    button.click()

    WebDriverWait(browser, 3).until(es.title_is('Главная'))
    assert browser.title == 'Главная'
    button = browser.find_element_by_class_name('header__button-create-bundle')
    button.click()
    WebDriverWait(browser, 3).until(es.title_is('Новый список'))
    assert browser.title == 'Новый список'
    name = browser.find_element_by_name('name')
    name.send_keys('Новое важное дело')
    button = browser.find_element_by_id('login-submit-btn')
    button.click()
    WebDriverWait(browser, 3).until(es.title_is('Главная'))
    new_list = browser.find_element_by_class_name('table-row_table_cell-1')
    assert new_list.text == 'Новое важное дело'
    browser.close()
