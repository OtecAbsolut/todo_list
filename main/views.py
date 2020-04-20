from django.shortcuts import render


data = {
    'lists': [
        {'id': 1, 'name': 'Позвонить', 'is_done': True, 'date': '29.12.2020'},
        {'id': 2, 'name': 'Написать', 'is_done': False, 'date': '30.12.2020'},
        {'id': 3, 'name': 'Заказать', 'is_done': False, 'date': '31.12.2020'},
        {'id': 4, 'name': 'Заказать', 'is_done': False, 'date': '31.12.2020'},
        {'id': 5, 'name': 'Заказать', 'is_done': False, 'date': '31.12.2020'}
    ],
    'user_name': 'Admin',
}


def main_view(request):
    context = data
    return render(request, 'index.html', context)


def edit_view(request, pk):

    return 'Hello'
