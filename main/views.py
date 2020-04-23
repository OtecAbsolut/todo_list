from django.shortcuts import render
from main.models import ListModel


def main_view(request):
    """ главная view """
    user = request.user
    lists = ListModel.objects.filter(
        user=user,
    ).order_by(
        'created'
    )
    context = {
        'lists': lists,
        'user': user.username
    }
    return render(request, 'index.html', context)


def edit_view(request, pk):
    return 'Hello'
