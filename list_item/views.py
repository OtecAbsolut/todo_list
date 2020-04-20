from django.shortcuts import render

data = {
    'lists': [
        {'name': 'Позвонить', 'is_done': True, 'date': '29.12.2020'},
        {'name': 'Написать', 'is_done': False, 'date': '30.12.2020'},
        {'name': 'Заказать', 'is_done': False, },
        {'name': 'Заказать', 'is_done': False, 'date': '31.12.2020'},
        {'name': 'Заказать', 'is_done': False, 'date': '31.12.2020'}
    ],
    'user_name': 'Admin',
}


def list_item_view(request):
    context = data
    return render(request, 'list.html', context)
