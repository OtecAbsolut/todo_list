# УРОК 5
- разминка для хвоста
```python
calculator = Calculator(10)
print(calculator.plus(5).minus(3).calc())
# 12
calculator2 = Calculator(12)
# 9
print(calculator2.plus(5).minus(3).minus(6).plus(1).calc())
```
- Разбор д\з
- Форма Логин\пароль
- View Логин\пароль
```python
def login_view(request):
    """
    Контроллер, который рендерит страницу авторизации.
    В случае успешной авторизации редиректит на главную
    """
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        success_url = reverse('main:main')

        if form.is_valid():
            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user and user.is_active:
                login(request, user)
                return redirect(success_url)

    return render(request, 'login.html', {'form': form})
```
- Создание ного списка дел (View)
```python
def create_new_list(request):
    """
    Обработка запроса на создание нового списка
    """
    form = ListForm()
    success_url = reverse('main:main')

    if request.method == 'POST':
        name = request.POST.get('name')
        form = ListForm({
            'name': name,
            'user': request.user
        })

        if form.is_valid():
            form.save()

            return redirect(success_url)

        form = ListForm()

    return render(request, 'new_list.html', {'form': form})
```
- Привязка своих стилей к форме
- Вывод ошибок валидации пользователю
- Форма редактирования списка
- Удаление списка
- Пагинация страниц
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
- Пагинация
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

д\з
- разлогирование пользователя
- Кнопка назад
```python
from django.contrib.auth import logout
```