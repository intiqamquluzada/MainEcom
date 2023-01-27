from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductImage, Size, Category
from django.db.models import F
from django.core.paginator import Paginator
from services.filter import ProductFilter
from .forms import ProductForm
from django.contrib import messages


def product_list_view(request):
    context, query_params = {}, ""
    products = Product.objects.annotate(
        total_price=F('price') + F('tax') - F('discount')
    ).order_by('-created_at')

    products, query_params = ProductFilter(request, products, query_params).filter_products()

    paginator = Paginator(products, 1)
    page = request.GET.get("page", 1)
    product_list = paginator.get_page(page)

    context['categories'] = Category.objects.order_by('-created_at')
    context['products'] = product_list
    context['sizes'] = Size.objects.order_by('-created_at')
    context['paginator'] = paginator
    context['query_params'] = query_params

    return render(request, 'list.html', context)


def product_create_view(request):
    context = {}
    form = ProductForm()

    if request.method == "POST":
        print("POST DATA: ", request.POST)
        print("FILES DATA: ", request.FILES)
        form = ProductForm(request.POST or None)
        files = request.FILES.getlist("image")
        if form.is_valid() and len(files)>=1:
            new_product = form.save()
            for file in files:
                ProductImage.objects.create(
                    product=new_product,
                    image=file
                )
            messages.success(request, f"{new_product.name} added!")
            return redirect("products:create")

    context["form"] = form
    return render(request, "create.html", context)
