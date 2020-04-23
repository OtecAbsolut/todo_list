# УРОК №2
## БД подключение, донастройка рабочего окружения
- Какие БД поддерживает джанга
- Почему PostgresSQL?  
https://postgrespro.ru/education/courses
- Команды для активации виртуального окружения   

**windows**
```yaml
deactivate
venv\Scripts\activate.bat
```
**mac\linux**
```yaml
deactivate
source venv\bin\activate
```
- Установка драйверов **pip install psycop2**
- Прописать базу в settings.py
```python
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "127.0.0.1",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "fred",
        "PORT": 5432
    }
}
```
- Миграции
https://docs.djangoproject.com/en/3.0/topics/migrations/
```yaml
python manage.py migrate
python manage.py makemigrations
python manage.py showmigrations
```
- Создание суперпользователя
```yaml
python manage.py createsuperuser
```
- Изучили, служебные таблицы
## Templates
https://docs.djangoproject.com/en/3.0/ref/templates/
## Д\З
- Повторить проделанные нами операции по подключению БД
- Создать новое приложение(app) **django-admin startapp list_item**
- Написать к нему вьюху
- Сделать шаблон(template) по аналогии с main и заполнить данными из словаря

- Добавить стиль CSS "id_done" в верстку
- *Создать свой **templatetag**, и с помощью него реализовать следующую задачу 
(на главной странице).  
У нас на странице создается столько строк, сколько мы передаем строк данных,
но выглядит не очень красиво если строк мало. 
Нужно (только средствами языка шаблонов) сделать так, чтобы
если нам передается строк меньше чем **6шт**, добить пустыми div блоками 
страницу, чтобы в сумме было 6шт блоков.  
-> Например 3 заполненных, 3 пустых.  
-> Если передаем 5 строк с данными то соответсвенно 5 заполненных 1 пустой.  
-> Если передаем 8 строк с данными - 8 заполненных блоков.  

Пример:  
![img](img/1.png)


Ссылка на документацию:
https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/  
Не забываем также создать папку **templatetags**, в которой нужно разместить модуль с функцией тега:  
![dir](img/2.png)

Также нужно дополнительно зарегистрировать нашу библиотеку тегов в 
**settings.py**  
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'main.templatetags'
]
```
И подгрузить библиотеку тегов на страницу шаблона:  
![dir](img/3.png)

# УРОК №3
## Наследование шаблонов
- теги block, extend
```
{% extends 'master.html' %}

{% block title %}
    <title>Главная</title>
{% endblock %}

{% block name_list %}
    <div class="table-data_table-header-item-1">TO DO List</div>
{% endblock %}
```
## Оптимизация роутинга URL
- функций include, и app_name = 'main'
```python
# \todo_list_ngu\todo_list_ngu\urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('list/', include('list.urls')),
]

# \todo_list\main\urls.py
app_name = 'main'

urlpatterns = [
    path('', main_view, name='main'),
    path('create/', create_new_list, name='create')
]
```
- Обрашение в темплейте по app_name
```python
 <a href='{% url "main:edit" pk=list.id %}'>
```
## Django ORM
Архитектура MVC  
![mvc](img/4.png)

ORM (англ. Object-Relational Mapping, рус. объектно-реляционное отображение, или 
преобразование) — технология программирования, которая 
связывает базы данных с концепциями объектно-ориентированных языков программирования  

**Django ORM Cookbook**  
https://prglb.ru/3h66k

**Офиц. документация**  
https://docs.djangoproject.com/en/3.0/ref/models/querysets/#



Рассмотрим:
- Проектирование БД  
https://docs.google.com/spreadsheets/d/1He-IVLLfwQv6MOhD6RbKyt3sItyfoAXgc98_c3ZSIo8/edit?usp=sharing
- model.Model
- Создание модели ListModel, типы данных
- Миграции
- Подключение модели к Админке  

main\admin.py
```python
from django.contrib import admin
from main.models import ListModel


class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'user']
    list_filter = ['created', 'name', 'is_done', 'user']
    search_fields = ['name', 'user']


admin.site.register(ListModel, ListAdmin)
```

## Д\З
- Синхронизировать код.
- Создание модели ListItemModel
- Миграции
- Добавить ListItemModel в админку

# УРОК №4
## Django ORM продолжение...
- Дескрипторы
```python
class AgeCheck:
    """
    Дескриптор
    """
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if value < 18:
            raise ValueError('Меньше 18 лет')
        instance.__dict__[self.name] = value


class Human:

    age = AgeCheck()

    def __init__(self, name, age):
        self.name = name
        self.age = age


man = Human('Bob', 15)
```
- Менеджер модели objects, и основные его методы
```python
item = Model.objects.get(id=1)
items = Model.objects.filter(id=1)
item.name = 'New name'
item.save()
item.delete()
order_by('id')
ListItem.objects.filter(list__user__username='Admin')
```
- Debug => QuerySet=> SQL 
- Ленивый QuerySet  

![cat](img/5.png)

- ? дебагер с SQL запросами
```python
LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}
```
## Django - forms
### Регистрация и логин
https://docs.djangoproject.com/en/3.0/ref/forms/api/
- Новое **application** для регистрации пользователей
- Форма регистрации пользователя

```python
class CustomUserCreationForm(UserCreationForm):
    """
    Форма регистрации нового пользователя.
    С обязательными полями: ['username', 'password', 'email']
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
```
- Шаблон формы регистрации
- View обработка регистрационных данных
```python
def create_user(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        success_url = reverse('main:main')

        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'registration.html', {'form': form})
```  
- ПОДСКАЗКА К ДЗ => Форма нового списка
```python
class ListForm(forms.ModelForm):
    """
    Форма натсроек расписания обмена
    """
    name = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = ListModel
        fields = ('name', 'user')
```


## Д\З
- Переделать шаблон **list.html** с наследованием от **master**
- Сделать динамические ссылки на list_items
![](img/6.png)
- Сделать **list_item_view** по отрисовки эелементов списков.
По аналогии с главной вьюхой приложения main.
Т.е. при клике на название списка, должна открываться страница списка
- Форма создания нового списка дел (кнопка "+")
- Вьюха создания нового списка
- Шаблон создания нового списка
