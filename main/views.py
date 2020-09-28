from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import *
from django.contrib.auth.models import auth
from account.models import *
from django.contrib import messages


def home(request):
    all_category = Category.objects.all()
    context = {
        "categories": all_category
    }
    return render(request, 'main/home.html', context)


def category(request):
    if 'sub_category' in request.GET:
        sub_category_id = request.GET['sub_category']
        all_product = Product.objects.filter(sub_category_id=sub_category_id)
        context = {
            "products": all_product
        }
        return render(request, 'main/posts.html', context)

    elif 'category' in request.GET:
        category_id = request.GET['category']
        category = Category.objects.get(id=category_id)
        all_product = Product.objects.filter(
            sub_category__category__id=category_id)
        context = {
            "products": all_product,
            "category": category
        }
        return render(request, 'main/posts.html', context)

    else:
        return HttpResponse('404 not found')


def postDetails(request, id):
    product = Product.objects.get(id=id)
    product.views = product.views + 1
    product.save()
    context = {
        'product': product
    }
    return render(request, 'main/details.html', context)


def login(request):
    if request.method == 'POST':
        number = request.POST['p_number']
        password = request.POST['password']
        user = auth.authenticate(username=number, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(
                request, 'invalid info please make sure username & password')
            return render(request, 'main/details.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'main/signup.html')

    elif request.method == 'POST':
        number = request.POST['number']
        f_name = request.POST['f-name']
        l_name = request.POST['l-name']
        password = request.POST['password']
        user = User.objects.create_user(
            username=f_name, email=number, password=password)
        user.save()
        customer = Customer_details(first_name=f_name, last_name=l_name)
        customer.save()
        return redirect('Confirm-signup-page')


def c_signup(request):
    # if request == 'GET': Otp confirmation part backend i did not solved.
    return render(request, 'main/signup-confirm.html')

    if request.method == 'POST':
        # otp = request.POST['otp'] This time we dont need otp.
        password = request.POST['password']
        c__password = request.POST['c__password']

        nxt_customer = Customer_details(
            password=password, c_password=c__password)
        nxt_customer.save()
        return redirect('/')


def create(request):

    category = Category.objects.all()
    context ={
        'category': category
    }

    return render(request, 'main/addposts.html', context)
