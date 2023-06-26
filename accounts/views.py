from cmath import log
from tkinter import E
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from .models import Profile
from products.models import *
from accounts.models import Cart , CartItems,SizeVariant
from django.http import HttpResponseRedirect
import razorpay
from django.conf import settings
from django.contrib.auth.decorators import login_required



def login_page(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')

        

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/login.html')


def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/register.html')




def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')
    

def add_to_cart(request,uid):
    variant = request.GET.get('variant')
    product = Product.objects.get(uid = uid)
    user = request.user
    cart , _ = Cart.objects.get_or_create(user=user,ispaid = False)
    cart_items = CartItems.objects.create(cart = cart,product = product)

    if variant:
        variant = request.GET.get('variant')
        size_variant = SizeVariant.objects.get(size_name = variant)
        cart_items.size_variant =  size_variant
        cart_items.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cart(request):
    cart_obj = None
    try:
      cart_obj = Cart.objects.get(user=request.user, ispaid=False)
    except Exception as e:
        print(e)

    if request.method == 'POST':
        cpn = request.POST.get('coupon')
        coupon_obj = Coupon.objects.get(coupon_code = cpn)
        if not coupon_obj:
            messages.warning(request,"invalid coupon")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        if cart_obj.coupon:
            messages.warning(request,"Coupon already exist")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        if cart_obj.get_cart_total() < coupon_obj.mininum_amount:
            messages.warning(request,f'Amount is greater than {{coupon_obj.mininum_amount}}')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        if coupon_obj.is_expired:
            messages.warning(request,"Coupon is expired")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        cart_obj.coupon = coupon_obj
        cart_obj.save()
        
        messages.success(request,"Coupon applied ")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    payment =None
    context = {'cart':cart_obj ,'payment':payment}
    
    if cart_obj.get_cart_total():
        client = razorpay.Client(auth=(settings.KEY,settings.SECRET))
        data = { "amount": cart_obj.get_cart_total(), "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
        cart_obj.razor_pay_order_id = payment['id']
        cart_obj.save()
        context = {'cart':cart_obj ,'payment':payment}

    return render(request,'accounts/cart.html',context)


def remove_cart(request,cart_item_uid):
    try:
        cart_item = CartItems.objects.get(uid = cart_item_uid)
        cart_item.delete()
        messages.success(request,"Coupon Removed ")
        
    except Exception as e:
        print(e)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def remove_coupon(request,uid):
    try:
        cart = Cart.objects.get(uid = uid)
        cart.coupon = None
        cart.save()
    except Exception as e:
        print(e)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def success(request):
    print('yes')
    order_id = request.GET.get('order_id')
    cart = Cart.objects.get(razor_pay_order_id = order_id)
    # cart.ispaid=  True
    # cart.save()
    context = {'cart':cart}
    return render(request,'pdf/invoice.html',context)
    return HttpResponse('payment success')


# @login_required
# def profile(request):
    # if request.method == 'POST':
    #      u_form = UserUpdateForm(request.POST ,instance=request.user)
    #      p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
    #      if u_form.is_valid() and p_form.is_valid():
    #          u_form.save()
    #          p_form.save()
    #          messages.success(
    #               request, f' Update successfully')
    #          return redirect('profile')
    # else:
    #     u_form = UserUpdateForm( instance=request.user)
    #     p_form = ProfileUpdateForm(instance=request.user.profile)


    # context = {
    #     'u_form':u_form,
    #     'p_form':p_form
    # }
    # print(request.user)
    # return render(request,'accounts/profile.html',request.user)


