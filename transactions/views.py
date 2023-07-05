from django.shortcuts import render, redirect
from transactions.forms import TransferForm
from customers_app.models import Users, Customers, Account
from transactions.models import Transactions
from django.contrib import messages

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
            
         
            amount = conversion(amount)
            user_balance = request.user.account
            user_balance = conversion(user_balance)
            
            receiver_name = Account.objects.get(account_number=receiver).account_name
            user_name = Account.objects.get(owner=request.user).account_name

            # context = {
            #     'form': request.POST,
            #     'account': receiver_name,
            # }
          

            if Account.objects.filter(account_number=receiver).exists():
                receiver_balance  = Account.objects.get(account_number=receiver)
                receiver_balance = conversion(receiver_balance)
                
                print(receiver_balance)
                if user_balance <= amount:
                    print('not enough funds')
                    return render(request, 'transact/transfer.html')
                else:
                    new_user_amount = user_balance - amount
                    new_receiver_amount = receiver_balance + amount
                    print(new_receiver_amount, new_user_amount)

                    updated_receiver = Account.objects.filter(account_number=receiver).update(balance=new_receiver_amount)
                    updated_user = Account.objects.filter(owner=request.user).update(balance=new_user_amount)
                    
                    current_user = Account.objects.get(owner=request.user)
                    print(current_user)
                    transaction = Transactions.objects.create(transferer=current_user, transferer_name=user_name, receiver=receiver_name, receiver_acct=receiver, amount=amount, remark=remark, alert_type=alert)
                    transaction.save()

                    time.sleep(4)
                    messages.success(request, 'Transaction successful!')
                    return redirect('transfer')

            else:
                print('does not exist')
                messages.error(request, 'Account does not exist!')    

    else:
         print('user not logged in')
         messages.info(request, 'You must be logged in first')
         return redirect('login')
    
  


    return render(request, 'transact/transfer.html')
