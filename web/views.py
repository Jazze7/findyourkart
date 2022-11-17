from django.shortcuts import render, get_object_or_404

from products.models import Product, Category, Brand

# Create your views here.


def index(request):
    Products = Product.objects.filter(is_deleted=False)

    categories = Category.objects.all()[:5]
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


def product(request, id):
    instances = get_object_or_404(Product.objects.filter(id=id))
    context = {
        "instances": instances,
        "title": "Product"
    }
    return render(request, "web/products.html", context=context)
