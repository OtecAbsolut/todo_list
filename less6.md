# УРОК 5
- Зарядка для хвоста
```python
# 1
a = [1, 2, 3]
b = a
a = a + [4, 5]
print(a, b, sep='\n')

# 2
row = [' '] * 3
print(row)
board = [row] * 3
print(board)
board[0][0] = 'x'
print(board)
```
- Вывод ошибок валидации пользователю
```python
 error_messages = {
            'username': {
                'unique_together': "Имя другое введи...",
                'unique': "Имя другое введи..."
            }
        }
```
- Ограничения в ДБ
```python
class Meta:
    unique_together = ('accounting_method', 'account')
```
- Индексы (Теория)
- Декоратор login_required
```python
from django.contrib.auth.decorators import login_required
@login_required(login_url='registration/login/')
```
- Форма редактирования списка
- Пагинация страниц

```python
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

PAGE_COUNT = 6
def view_with_pagination(request):
    context = {}
    lists = ListModel.objects.filter(
        user=request.user,
    ).order_by(
        'created'
    )
    paginator = Paginator(lists, PAGE_COUNT)
    page = request.GET.get('page')

    try:
        list_page = paginator.page(page)
    except PageNotAnInteger:
        list_page = paginator.page(1)
    except EmptyPage:
        list_page = paginator.page(paginator.num_pages)

    context['lists'] = list_page
    context['pages'] = list(paginator.page_range)
    context['user'] = request.user.username

    return render(request, 'index.html', context)
```
- Отрисовка в шаблоне
```python
{% block empty_div %}
    {% if lists|length < 6 %}
        {% for _ in lists|get_count %}
            <div class="table-data__table-row">
                <div class="table-row_table_cell-1"></div>
            </div>
        {% endfor %}
    {% endif %}
    {% if pages.1 %}
        <div class="table-data__table-row">
            <div class="paginator_class">
                <ul class="pagination-wrapper_button">
                    {% for page in pages %}
                        <li><a class="active" href="/?page={{ page }}">{{ page }}</a></li>
                    {% endfor %}
                </ul>
            </div>
        </div>
    {% endif %}
{% endblock %}
```
- *Generic
```python
class RegistrationUserView(CreateView):
    """
    Generic для обновления расписания на страницы настроек
    """
    model = User
    template_name = 'registration.html'
    success_url = reverse_lazy('registration:login')
    form_class = CustomUserCreationForm
```

##Д\З
- Предыдущее 
```python
def list_item_view(request, pk):
    user = request.user
    list_items = ListItem.objects.filter(
        list=pk,
    ).order_by(
        'created'
    )
    list_name = ListModel.objects.filter(id=pk).first()
    context = {
        'list_items': list_items,
        'user': user.username,
        'list_name': list_name.name
    }
    return render(request, 'list.html', context)
```
- Кнопка "Разлогирование пользователя"
```python
from django.contrib.auth import logout
```
- Форма создание нового элемента списка
    - Добавить в форму создания элемента списка поле дату
- Форма редактирования элемента списка
- Добавить ограничение на поле **name** в эелементах списка
- Добавить вывод предупреждения в форму при попытки добавить дело
с уже существующем именем 
- Пагинация на странице list.html
- Добавить login_required
