# urls for products app
from django.urls import path
from .views import ProductList

urlpatterns = [
    path('', ProductList.as_view()),
]
