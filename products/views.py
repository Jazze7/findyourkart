from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.forms import ProductForm

# Create your views here.


@login_required(login_url="/users/login/")
def create(request):
    if request.method == 'POST':
        pass
    else:
        form=ProductForm
        context = {
            "title":"Create new product",
            "form" : form
         }
        return render(request, "products/create.html", context=context)
