from django.shortcuts import render, redirect
from transactions.forms import TransferForm
from customers_app.models import Users, Customers, Account
import time


def conversion(var):
    var = str(var)
    var = float(var)
    var = int(var)
    return var



def loadTransferPage(request):
    users = Users.objects.all()
    customers = Customers.objects.all()

    if request.user.is_authenticated is True:
        print('yes')
        print(request.method)
        if request.method == 'POST':
            print('okay')
            receiver = request.POST.get('receiver')
            amount = request.POST.get('amount', False)
            alert = request.POST.get('alert')
            remark = request.POST.get('remark')
            pin = request.POST.get('pin')
            # username = request.POST.get('user')

            print(receiver, amount, type(amount), alert, pin)

            if Account.objects.filter(account_number=receiver).exists():
                account_owner  = Account.objects.get(account_number=receiver)
                time.sleep(3)
                
                
                
        
            else:
                print('does not exist')
            

    else:
         print('user not logged in')
         return render(request, 'transact/transfer.html')
        
    
    context = {
        'account': account_owner,
    }

    return render(request, 'transact/transfer.html', context)
