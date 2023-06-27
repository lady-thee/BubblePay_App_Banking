from django.shortcuts import render, redirect
from django.urls import reverse
from customers_app.forms import CustomerCreationForm, UsersCreationForm
from customers_app.models import Customers, Users, Account

from django.views.decorators import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.conf import settings

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generator_token

from django.core.mail import EmailMessage
import random


def createAccountNumber():
    prefix = ''
    for i in range(8):
        val = str(random.randint(1, 9))
        prefix += val
    account = str(33) + prefix
    return account
        # print(val)
        # print(tokens)




def createUser(email, password):
    user = Users.objects.create_user(email=email, password=password)
    return user


def activate_token(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Users.objects.get(pk=uid)
    except (ValueError, Users.DoesNotExist):
        user = None
    
    if user is not None and generator_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        messages.success(request, 'Successfully verified email')
        return redirect(reverse('signup'))
    else:
        messages.error(request, 'Verification link was invalid')
        return redirect(reverse('create'))


def sendActivationMail(user, request):
    current_site = get_current_site(request)
    email_subject = 'Verify your account'
    email_body = render_to_string(
        'auth/pages/confirm.html',
        {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generator_token.make_token(user),
        }, 
    )

    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )
    email.content_subtype = 'html'
    email.send()



def loadUserCreatePage(request):
    form = UsersCreationForm()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = UsersCreationForm(request.POST)
        confirm = request.POST.get('confirm_pass', False)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if Users.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
            else:
                if password != confirm:
                    messages.error(request, 'Passwords don\'t match!')
                else:
                    user = createUser(email, password)
                    messages.success(request, 'Successfully created!')
                    sendActivationMail(user, request)
                    
                    
        else:
            messages.error(request, 'Form is not validated')
            raise ValueError
            

    return render(request, 'auth/pages/usercreate.html', context)


def loadSignUpPage(request):
    profileform = CustomerCreationForm()
    userform = UsersCreationForm()
    context = {
        'user': userform,
        'profile': profileform,
    }
   
    if request.method == 'POST':
        userform = UsersCreationForm(request.POST)
        profileform = CustomerCreationForm(request.POST, request.FILES)
        account_num = createAccountNumber()
        confirm = request.POST.get('confirm_pass', False)
        if userform.is_valid() and profileform.is_valid():
            email = userform.cleaned_data['email']
            password = userform.cleaned_data['password']
            username = profileform.cleaned_data['username']
            firstname = profileform.cleaned_data['firstname']
            lastname = profileform.cleaned_data['lastname']
            mobile = profileform.cleaned_data['mobile']
            location = profileform.cleaned_data['location']
            bvn = profileform.cleaned_data['BVN']
            photo = profileform.cleaned_data['photo']
            print(email, account_num)
            if Users.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
            else:
                if password != confirm:
                    messages.error(request, 'Passwords don\'t match!')
                else:  
                    user = Users.objects.create_user(email=email, password=password)
                    messages.success(request, 'Successfully created!')
                    messages.info(request, 'Verify email using link in email')
                    sendActivationMail(user, request)
                    customers = Customers.objects.create(user=user, username=username, firstname=firstname, lastname=lastname, mobile=mobile, location=location, photo=photo, BVN=bvn)
                    account = Account.objects.create(owner=user, account_number=account_num)
                    customers.save()
                    account.save()
                    messages.success(request, 'Account successfully created!')
                       
        else:
            print(profileform.errors)
            

    return render(request, 'auth/pages/signup.html', context)


def loadLoginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print(user, request.user.is_authenticated)
            return redirect('dashboard')


    return render(request, 'auth/pages/login.html')

