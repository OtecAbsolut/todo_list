from django.urls import path
from list_item.views import list_item_view

app_name = 'list_item'

urlpatterns = [
    path('<int:pk>', list_item_view, name='list_item'),
    path('edit/', list_item_view, name='edit'),
    path('delete/', list_item_view, name='delete'),
]

