from django.urls import path
from registration.views import create_user, login_view, logout_view

app_name = 'registration'

urlpatterns = [
    path('new_user/', create_user, name='new_user'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
