from django.shortcuts import render, get_object_or_404
from .models import (Category, Product)
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    """
    retrieve a list(multiple) of products. Products is filtered based on availability or category_slug
    :param request:  HttpRequest contains metadata about the request such as scheme, body, method etc
    :param category_slug: optional parameter for filtering products according to a given category.
    :return: filtered products if available or from a category
    """
    category = None
    categories = Category.objects.all()  # get all categories
    products = Product.objects.filter(available=True)  # show only available products

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        # filter the products according to their category using the related_name in Product Model
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    """
    :param request: contains the scheme(http/https), body, path("/shop/causual-shirts/), method(GET/POST)
    :param id: ID is gotten automatically since it's a hidden field in every view
    :param slug: slug is included in the URL to build SEO-friendly URLs for products
    :return: Product instance through id and slug.
    """
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)