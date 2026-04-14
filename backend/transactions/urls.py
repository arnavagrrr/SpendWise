from django.urls import path
from .views import add_transaction, get_transactions, clear_transactions

urlpatterns = [
    path('add/', add_transaction),
    path('all/', get_transactions),
    path('clear/', clear_transactions),
]