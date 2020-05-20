# УРОК 10

## Unit и интеграционные тесты
- Тестирование view
```python
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
    response = csrf_client.post('/create/', data={
        'name': 'Тестовый список дел',
        'csrfmiddlewaretoken': csrf.value
    })
    assert response.status_code == 302, response.content.decode()

```

- Тестирование form

- Тестирование моделей

## Тестовое покрытие (Пример travis)
Мы проверяем, насколько набор проводимых тестов соответствует требованиям к продукту, 
а также анализируем полноту проверки тестами кода разработанной части продукта.  

```python
pip install pytest-cov
```
## TDD и BDD
- ТDD
![tdd](/img/tdd.png)  

- BDD => Cucumber/Behave
https://habr.com/ru/post/216923/  

```
FEATURE 1: На счету есть деньги+
GIVEN счет с деньгами
AND валидную карточку
AND банкомат с наличными
WHEN клиент запрашивает наличные
THEN убедиться, что со счета было списание
AND убедиться, что наличные выданы
AND убедиться, что карточка возвращена
```

### Рекомендации по литературе
Персиваль 

## ДЗ
- Тест **list_item_view**
- Тест **create_item_view** 
- Тест c Selenium на создание нового списка дел
- ***Решить проблему с пагинацией
