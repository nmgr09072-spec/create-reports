"""経費アプリの設定。"""
from django.apps import AppConfig


class ExpensesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "expenses"
    verbose_name = "経費管理"
