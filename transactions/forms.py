from django.forms import ModelForm
from django import forms 
from transactions.models import Transactions


class TransferForm(forms.ModelForm):
    
    class Meta:
        model = Transactions
        fields = ['transferer_name', 'receiver','receiver_acct', 'amount', 'remark', 'alert_type']
        widgets = {
            'receiver_acct': forms.TextInput(attrs={
                'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'account number',
                'required' : True,
                }),
            
            # 'receiver': forms.Select(attrs={
            #     'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            #     ''
            # })
        }