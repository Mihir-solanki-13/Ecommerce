from pydoc import render_doc
from tkinter import E
from django.shortcuts import render
from products.models import Product

def get_product(request , slug):
    try:
        product = Product.objects.get(slug =slug)
        context = {'product':product}
        updated_price = 0
        if request.GET.get('size'):
            size = request.GET.get('size')
            # print(size)
            price = product.get_product_by_size(size)
            updated_price+=price
            context['selected_size'] = size
            # print(price)

        if request.GET.get('color'):
            color = request.GET.get('color')
            # print(size)
            price = product.get_product_by_color(color)
            updated_price+=price
            context['selected_color'] = color
            # print(price)

        context['updated_price'] = updated_price
        return render(request  , 'product/product.html' , context =context)

    except Exception as e:
        print(e)

