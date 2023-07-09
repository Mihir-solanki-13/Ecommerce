from pydoc import render_doc
from tkinter import E
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
# from seller.models import Product
from products.models import Product,Category,ProductImage
import uuid

def generate_unique_value(value1, value2):
    unique_value = f'{value1}-{value2}-{uuid.uuid4()}'
    return unique_value

def index(request):
    if not hasattr(request.user, 'seller') or (request.user.seller is None or not request.user.seller.is_verified):
       messages.warning(request, 'Not Approved By Admin')
       return redirect('/')

    if request.method == 'POST':
        # Retrieve the form data submitted by the seller
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        print('mihir')
        category = Category.objects.get(category_name=category)
        print(category)
        product_desription = request.POST.get('product_description')

        # Retrieve the seller associated with the current user
        

        # Create a new product instance and populate it with the form data
        product = Product(
            product_name=product_name,
            slug=generate_unique_value(category,product_name),
            category=category,
            price=price,
            product_desription=product_desription,
            seller=seller
        )
        product.save()
        product_images = request.FILES.getlist('product_images')
        for image in product_images:
            # Create a ProductImage instance
            product_image = ProductImage(product=product, image=image)
            product_image.save()

        # Redirect or perform any other necessary actions
        return redirect('/')
    category = Category.objects.all()
    # print(category) 
    context={'category':category}
    return render(request, 'seller/sell.html',context)


# def index(request ):

#     return render(request  , 'seller/sell.html' )

    # try:
        # product = Product.objects.get(slug =slug)
        # return render(request  , 'product/product.html' , context = {'product' : product})

    # except Exception as e:
    #     print(e)

