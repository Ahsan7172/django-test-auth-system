from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    User={
        ('1','admin'),
        ('2','user')
        
    }
    user_type=models.CharField(choices=User,max_length=20,default='1')
bank_choice=(
    ('allied bank','allied bank'),
    ('hbl','hbl'),
    ('ubl','ubl')
)
class Bank(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    bank_name=models.CharField(choices=bank_choice,max_length=70)
    loan_type=models.CharField(max_length=70)
    creation_date=models.DateTimeField(auto_now_add=True)
    updation_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.bank_name
    

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Pending','Pending'),
    ('approved','approved')
   

)

class LoanRequest(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    bank=models.ForeignKey(Bank,on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    reason=models.TextField()
    amount=models.PositiveIntegerField()
    Date=models.DateField()
    interest_rate=models.DecimalField(max_digits=5,decimal_places=2)
    payable_amount=models.PositiveIntegerField()
    status=models.CharField(choices=STATUS_CHOICES,default='pending',max_length=70)
    def __str__(self):
        return self.user.username

class loanTransaction(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    transaction = models.UUIDField(
        primary_key=True, editable=False)
    payment = models.PositiveIntegerField(default=0)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class ReturnLoan(models.Model):
     user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
     loan_type=models.ForeignKey(Bank,on_delete=models.CASCADE)
     paid_amount=models.IntegerField()
     total_amount=models.IntegerField()
     creation_date=models.DateTimeField(auto_now_add=True)
     updation_date=models.DateTimeField(auto_now=True)
     
     
