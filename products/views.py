import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from products.forms import ProductForm
from products.models import Brand, Category, Product
from main.functions import generate_form_errors

# Create your views here.


@login_required(login_url="/users/login/")
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            tags = form.cleaned_data['tags']
            if not Brand.objects.filter(user=request.user).exists():
                brand = Brand.objects.create(
                    user=request.user, name=request.user.username)
            else:
                brand = request.user.brand
            instance = form.save(commit=False)
            instance.brand = brand
            instance.save()

            tags_list = tags.split(",")
            for tag in tags_list:
                category, created = Category.objects.get_or_create(
                    title=tag.strip())
                instance.categories.add(category)

            response_data = {
                "title": "Successfully submitted",
                "message": "Successfully submitted",
                "status": "success",
                "redirect": "yes",
                "redirect_url": "/"
            }
        else:
            error_message = generate_form_errors(form)
            response_data = {
                "title": "form validation error",
                "message": str(error_message),
                "status": "error",
                "stable": "yes",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    else:
        form = ProductForm()
        context = {
            "form": form,
            "title": "Create a new post"

        }
        return render(request, "products/create.html", context=context)
