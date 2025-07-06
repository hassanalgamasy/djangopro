from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    ACCOUNT_TYPES=(
    ('client','عميل'),
    ('company','شركه')
    )
    account_type=models.CharField(max_length=10, choices=ACCOUNT_TYPES, default='client',
                                  verbose_name='نوع الحساب')
    phone=models.CharField(max_length=15, unique=True, verbose_name='رقم الموبايل')
    balance=models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='الرصيد')
