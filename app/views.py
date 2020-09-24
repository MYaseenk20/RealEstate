from django.shortcuts import render,redirect
from .choice import bedroom_choices,state_choices,price_choices
# Create your views here.
from .models import Listings,Contact,Realtor
from .forms import Userform
from django.contrib.auth import authenticate,login as auth_login,logout
from .decorator import user_authenticated
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail


# main home page
def home(request):
    listings=Listings.objects.order_by('-publish_date').filter(public=True)
    context={'listings':listings,'price_choices':price_choices,'bedroom_choices':bedroom_choices,'state_choices':state_choices}
    return render(request,'app/index.html',context)

# about page
def about(request):
    realtors=Realtor.objects.all()
    context={'realtors':realtors}
    return render(request,'app/about.html',context)

# listing page where all houses are listing for sale
def listings(request):
    listings = Listings.objects.order_by('-publish_date').filter(public=True)
    context = {'listings': listings}
    return render(request,'app/listings.html',context)



def listing(request,pk):
    listing= Listings.objects.get(pk=pk)
    context = {'listing': listing}
    return render(request,'app/listing.html',context)


# register page
@user_authenticated
def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'This username already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This Email already taken')
                    return redirect('register')
                else:
                    user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
                    user.save()
                    messages.success(request,'Your account has been created')
                    return redirect('login')
        else:
            messages.error(request, 'Your Password do not match')
            return redirect('register')
    return render(request,'app/register.html')


# login page
@user_authenticated
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            messages.success(request,'Your login in now')
            return redirect('dashboard')

    return render(request,'app/login.html')
# logout
def logoutUser(request):
    logout(request)
    return redirect('login')

def search(request):
    qureylist=Listings.objects.order_by('-publish_date')
    if 'keywords' in request.GET:
        keyword=request.GET['keywords']
        if keyword:
            qureylist=qureylist.filter(zipcode__icontains=keyword)
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            qureylist=qureylist.filter(state__iexact=state)
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            qureylist=qureylist.filter(city__iexact=city)
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            qureylist=qureylist.filter(price__lte=price)
    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            qureylist=qureylist.filter(bedrooms__lte=bedrooms)


    context={'listings':qureylist,'price_choices':price_choices,'bedroom_choices':bedroom_choices,'state_choices':state_choices}

    return render(request,'app/search.html',context)

def contact(request):
    if request.method == 'POST':
        listing=request.POST['listing']
        listing_id=request.POST['listing_id']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']
        send_mail(
            'Realstate Listing Website',
            'There has been an inquiry for' + listing + '. Sign into the admin panel for more info',
            'my444323@gmail.com',
            [realtor_email,'yf20122001@gmail.com'],
            fail_silently=False,
        )
        contact=Contact(listing=listing,listing_id=listing_id,name=name,email=email,
                        phone=phone,message=message,user_id=user_id,
                        )
        contact.save()
        messages.success(request,'You request has been submitted and realtor will contact you soon')
        return redirect('/listing/'+listing_id)

def dashboard(request):
    contacts=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={'contacts':contacts}

    return render(request,'app/dashboard.html',context)

