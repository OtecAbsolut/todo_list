from django.shortcuts import render, reverse, redirect
from list_item.models import ListItem
from main.models import ListModel
from list_item.forms import ListItemForm


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
        'list_name': list_name
    }
    return render(request, 'list.html', context)


def create_item_view(request, pk):
    form = ListItemForm()

    if request.method == 'POST':
        name = request.POST['name']
        expire_date = request.POST['expire_date']
        form = ListItemForm({
            'name': name,
            'expire_date': expire_date,
            'list': pk
        })
        success_url = reverse('list_item:list_item', kwargs={'pk': 5})

        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'new_list_item.html', {'form': form})

