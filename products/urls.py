from django.urls import path, include
from products import views

app_name = "products"

urlpatterns = [
    path('create/', views.create, name='create')
]
