from django.contrib import admin
from .models import CustomUser,Bank,LoanRequest
# Register your models here.
@admin.register(CustomUser)
class AdminSpec(admin.ModelAdmin):
    list_display=['id','first_name','last_name','username','email','password','user_type']
@admin.register(LoanRequest)
class AdminLoan(admin.ModelAdmin):
    list_display=['id','user','bank','reason','amount','Date','interest_rate','payable_amount','status']
@admin.register(Bank)
class AdminBank(admin.ModelAdmin):
    list_display=['bank_name','loan_type','creation_date','updation_date']
