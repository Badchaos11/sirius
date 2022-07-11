from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path("new/", addpage, name="add_page"),
    path("update/", updatepage, name="update_page"),
    path("delete", deletepage, name="delete_page"),
]
