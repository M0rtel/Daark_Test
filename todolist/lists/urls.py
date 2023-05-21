from django.urls import path

from . import views

app_name = 'lists'
urlpatterns = [
    path("", views.home, name='home'),
    path("folder/<folder_id>/", views.folder_detail, name='folder'),
    path("list/<list_id>/", views.list_detail, name='detail'),
    path("login/", views.login, name='login'),
    path("register/", views.RegisterUser.as_view(), name='register'),
]
