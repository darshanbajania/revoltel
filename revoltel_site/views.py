from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from .models import Products, Customers, User_id, Purchase_details
from django.core.mail import send_mail
from .forms import ContactForm
from django.urls import reverse
from urllib.parse import urlencode
import json
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import requests

#Global Variables


total_amout = 0

# Create your views here.

def Home_view(request):
    return render(request, 'revoltel_site/base.html')

def About_us_view(request):
    return render(request, 'revoltel_site/about_us.html')

def Contact_us_view(request):
    if request.method == "POST":
        form_recieved = ContactForm(request.POST)
        name = request.POST.get('name')
        sender = request.POST.get('email')
        mobile = request.POST.get('ph_number')
        co_name = request.POST.get('co_name')
        query = request.POST.get('message')
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
                'secret': '6Lci0zQaAAAAAIiW-xsFlcgV6GK8bKYM4knvToik',
                'response': recaptcha_response
            }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        # print(name, sender, mobile, co_name,query)
        recipients = ['md@revoltel.in']
        subject = "Website Inquiry"
        message = "Name: "+name + "\nEmail Id: "+ sender + "\nMobile No: "+ str(mobile) +"\nCompany Name: "+ co_name+"\nQuery: " + query
        if result['success']:
            #send_mail(subject, message, 'md@revoltel.in', recipients)
            print('hello')
        #send_mail(subject, message, 'md@revoltel.in', recipients)
        # if form_recieved.is_valid():
        #     message = ""
        #     name = form_recieved.cleaned_data['name']
            
        #     mobile = form_recieved.cleaned_data['mobile']
            
        #     sender = form_recieved.cleaned_data['email']
            
        #     co_name = form_recieved.cleaned_data['co_name']
            
        #     query = form_recieved.cleaned_data['message']
        #     message = "Name: "+name + "\nEmail Id: "+ sender + "\nMobile No: "+ str(mobile) +"\nCompany Name: "+ co_name+"\nQuery: " + query
        #     subject = "Website Inquiry"
            

            
            # print(message)
            # send_mail(subject, message, 'md@revoltel.in', recipients)
    contact_form = ContactForm()
    context= {
        'form': contact_form,
    }

    return render(request, 'revoltel_site/contact_us.html',context)

def Product1_view(request):
    return render(request, 'revoltel_site/all_in_one_pbx.html')

def Product2_view(request):
    return render(request, 'revoltel_site/call_center_dialer.html')

def Product3_view(request):
    return render(request, 'revoltel_site/crm.html')

def Product4_view(request):
    return render(request, 'revoltel_site/hospital_pbx.html')

def Product5_view(request):
    return render(request, 'revoltel_site/multi_level_ivr.html')

def Product6_view(request):
    return render(request, 'revoltel_site/real_estate.html')

def Product7_view(request):
    return render(request, 'revoltel_site/telecom_consultant.html')

def Product8_view(request):
    return render(request, 'revoltel_site/virtual_extensions.html')

def Services_view(request):
    return render(request, 'revoltel_site/services.html')

def Login_View(request):
    # if session is there redirect to profile page
    if request.session.has_key('is_logged_in'):
        return redirect('trading_site:home')
        
    if request.method == 'POST':  # authanticate user using login page

        # getting the username of current user
        username = request.POST.get('username')
        # getting the password of current user
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        # authenticating current user
        user = authenticate(username=username, password=password)
        # print(user)
        if user is not None:  # A backend authenticated the credentials
            login(request, user)  # logging in the current user
            # make the session true after logging in
            request.session['is_logged_in'] = True
            current_user = Customers.objects.filter(user = request.user).first()
            if current_user.customer_id == "no_id":
                user_id = User_id.objects.all().first()
                current_user.customer_id = int(user_id.new_user_id)
                current_user.save()
                user_id.new_user_id = str(int(user_id.new_user_id)+1)
                user_id.save()
            
            if (username == 'admin'):  # if user is admin redirect it to admin_page
                return redirect('trading_site:admin_page')
            else:
                return redirect('revoltel_site:home_page')  # else to the user profile

        else:
            # No backend authenticated the credentials
            return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')


# Shows page to register a new user
def register_view(request):
    # if sessions are there redirect to profile page
    if request.session.has_key('is_logged_in'):
        return redirect('revoltel_site:home_page')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # form for creating new user
        if form.is_valid():  # if valid then create new user and redirect to login page
            form.save()
            return redirect('revoltel_site:login_view')
    else:  # if form is not correct redirect to the the reggister page with a form
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})    


def Shop_view(request):
    if request.session.has_key('cart_contents') != True :
        request.session['cart_contents'] = {}
    if request.session.has_key('cart_contents'):
        cart_contents = request.session['cart_contents']
        # print(request.session['cart_contents'])
        all_products = Products.objects.order_by('product_id')
        if request.method == "POST":
            cart_product_number = request.POST.get('product_id')
            if cart_product_number != None:
                cart_product = Products.objects.filter(product_id = cart_product_number).first()
                cart_contents[cart_product.product_id] = 1 
                request.session['cart_contents'] = cart_contents
                # cart_contents.clear()
                # print(cart_contents)
                # print(request.session['cart_contents'])
            product_number = request.POST.get('view_id')
            if product_number != None:
                # getting the url for displaying full proposal
                print(product_number)
                base_url = reverse('revoltel_site:product_view_page')
                # creating a string of dictionary
                query_string = urlencode({'category': product_number})
                # passing the base_url and query from this page to url
                url = '{}?{}'.format(base_url, query_string)

                # print(proposal_number)
                return redirect(url)
    context = {
        'cart_page' : True,
        'all_products' : all_products,
        'cart_contents': cart_contents,
    }
    return render(request, 'revoltel_site/shop.html',context)

def Product_view_page(request):
    if request.session.has_key('cart_contents'):
        cart_contents = request.session.get('cart_contents')
        current_product_id = request.GET.get('category')
        # print(current_product_id) 
        selected_product = Products.objects.filter(product_id=current_product_id).first()
        if request.method == "POST":
            product_page_quantity = request.POST.get('Quantity')
            cart_contents[selected_product.product_id] = product_page_quantity
            request.session['cart_contents'] = cart_contents
            # print(cart_contents)

    context = {
        'selected_product':selected_product,
        'cart_page' : True,
        'cart_contents': cart_contents,
    }
    return render(request, 'revoltel_site/product_view_page.html',context)

def Cart_view(request):
    if request.session.has_key('cart_contents'):
        cart_contents = request.session.get('cart_contents')
        cart_contents_description = []
        bill_description = []
        total_amount = 0
        if request.method == "POST":
            if request.POST.get('add') != None:
                item_id = request.POST.get('product_id')
                # print(type(item_id))
                # print(cart_contents.get(int(item_id)))
                cart_contents[item_id] = int(cart_contents.get(item_id)) + 1
                request.session['cart_contents'] = cart_contents
            if request.POST.get('minus') != None:
                item_id = request.POST.get('product_id')
                # print(type(item_id))
                # print(cart_contents.get(int(item_id)))
                cart_contents[item_id] = int(cart_contents.get(item_id)) - 1
                if cart_contents[item_id] == 0:
                    cart_contents.pop(item_id)
                    request.session['cart_contents'] = cart_contents


            if request.POST.get('remove') != None:
                item_id = request.POST.get('product_id')
                # print(type(item_id))
                # print(cart_contents.get(int(item_id)))
                cart_contents.pop(item_id)
                request.session['cart_contents'] = cart_contents


        for cart_item_id,quantity in cart_contents.items():
            product_info = []
            bill_info = []
            total_info = 0
            product_info.append(cart_item_id)
            prod = Products.objects.filter(product_id=cart_item_id).first()
            product_name = prod.product_name
            bill_info.append(prod.product_name)
            product_info.append(product_name)
            product_image_url = prod.product_image.url
            product_info.append(product_image_url)
            product_price = prod.price
            product_info.append(product_price)
            product_info.append(quantity)
            bill_info.append(quantity)
            cart_contents_description.append(product_info)
            bill_info.append(int(quantity)*int(product_price))
            bill_description.append(bill_info)
            total_amount = total_amount + int(quantity)*int(product_price)
            request.session['total_amount'] = total_amount
    # print(bill_description,total_amount)
    context={
        'cart_content':cart_contents,
        'cart_items':cart_contents_description,
        'bill_description': bill_description,
        'total_amount': total_amount,
    }
    return render(request, 'revoltel_site/cart.html',context)


def Checkout_view(request):
    c_name=''
    c_email=''
    c_number=''
    c_address=''
    if request.method == "POST":
        c_name = request.POST.get('name')
        c_email = request.POST.get('email')
        c_number = request.POST.get('ph_number')
        c_address = request.POST.get('address')
        flag = 1
        customer_details =[]
        customer_details.append(c_name)
        customer_details.append(c_email)
        customer_details.append(c_number)
        customer_details.append(c_address)
        request.session['customer_info'] = customer_details
    else:
        flag= 2
    total_amout = request.session['total_amount']

    # if request.body:
    #     body = json.loads(request.body)
    #     customer_details.append(body['customer_name'])
    #     customer_details.append(body['customer_email'])
    #     customer_details.append(body['customer_no'])
    #     customer_details.append(body['customer_address'])
    #     request.session['customer_info'] = customer_details 
    context = {
        'flag':flag,
        'c_name':c_name,
        'c_email':c_email,
        'c_number':c_number,
        'total_amount':total_amout,
    }
    # print(total_amout)      
    return render(request, 'revoltel_site/payment_page.html',context)

def Payment_complete_view(request):
    cart = request.session['cart_contents']
    cart_contents = ""
    form_value_check = "1"
    trxn_order_id = ""
    # print("outside")
    if request.method == "POST":
        trxn_order_id = request.POST.get('trxn_order_id')
        # print("inside post")
        if trxn_order_id != None:
            # print("changeing check value")
            form_value_check = "0"

    # print(cart)
    # print(bool(cart))
    if bool(cart):
        for cart_item,values in cart.items():
            cart_content_product_info=""
            cart_product = Products.objects.filter(product_id = cart_item).first()
            cart_content_product_info = cart_product.product_name + " X (" + str(values) + "): ₹" + str(int(cart_product.price)*values)
            cart_contents = cart_contents + "\n" +cart_content_product_info
            # print(cart_content_product_info)
        customer_detail = request.session['customer_info']
        customer_info = ""
        for customer_info_item in customer_detail:
            customer_info = customer_info +customer_info_item + "\n\n"
        total_amount = request.session['total_amount']
        message ="Payment Order Id: "+ trxn_order_id + "\n\nCUSTOMER INFO:\n\n"+ customer_info + "\n\n\nPurchased Products:\n\n" + cart_contents + "\n\nTotal Amount:" + str(total_amount)
        recipients = ['md@revoltel.in']
        subject = "Purchase Order from "+ customer_detail[0]
        send_mail(subject, message, 'md@revoltel.in', recipients)
        cart_empty = {}
        request.session['cart_contents'] = cart_empty

    # print(customer_detail[1])
    # print(request.session['cart_contents'])
    
    context = {
        'form_value_check' : form_value_check,
    }
    return render(request, 'revoltel_site/payment_complete_page.html',context)