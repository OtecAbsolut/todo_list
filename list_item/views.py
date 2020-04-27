from django.shortcuts import render, reverse, redirect
from list_item.models import ListItem
from main.models import ListModel


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



