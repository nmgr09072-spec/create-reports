"""経費アプリの URL 設定。"""
from django.urls import path

from . import views

app_name = "expenses"

urlpatterns = [
    path("", views.expense_list, name="list"),
    path("add/", views.expense_add, name="add"),
    path("delete/<int:pk>/", views.expense_delete, name="delete"),
    path("sites/", views.site_list, name="sites"),
    path("sites/delete/<int:pk>/", views.site_delete, name="site_delete"),
    path("api/sites/", views.api_sites, name="api_sites"),
]
