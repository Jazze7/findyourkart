from django.shortcuts import render
from products.models import Product, Category, Brand

# Create your views here.


def index(request):
    Products = Product.objects.filter(is_deleted=False)

    categories = Category.objects.all()
    brands = Brand.objects.all()

    search_brand = request.GET.getlist("brand")
    print(search_brand)
    if search_brand:
        Products = Product.objects.filter(brand__in=search_brand)

    search_categories = request.GET.getlist("category")
    if search_categories:
        Products = Product.objects.filter(
            categories__in=search_categories).distinct()
    context = {
        "title": "Find Your Kart",
        "products": Products,
        "categories": categories,
        "brands": brands
    }
    return render(request, "web/index.html", context=context)
