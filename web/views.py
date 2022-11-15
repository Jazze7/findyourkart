from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):
    Products = Product.objects.filter(is_deleted=False)
    context = {
        "title": "Find Your Kart",
        "products": Products
    }
    return render(request, "web/index.html", context=context)
   