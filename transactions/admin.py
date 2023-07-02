from django.contrib import admin
from transactions.models import Transactions


class TransactionsAdmin(admin.ModelAdmin):
    model = Transactions
    list_display = ['transferer', 'transferer_name', 'receiver', 'receiver_acct', 'amount', 'remark', 'alert_type', 'time_processed']
    list_display_links = ['transferer_name', 'receiver']



admin.site.register(Transactions, TransactionsAdmin)
