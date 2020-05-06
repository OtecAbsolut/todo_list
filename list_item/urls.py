from django.urls import path
from list_item.views import (
    list_item_view, create_item_view, edit_list_item_view, done_view
)

app_name = 'list_item'

urlpatterns = [
    path('<int:pk>', list_item_view, name='list_item'),
    path('edit/<int:pk>', edit_list_item_view, name='edit'),
    path('delete/', list_item_view, name='delete'),
    path('create/<int:pk>', create_item_view, name='create'),
    path('done/', done_view, name='done'),
]

