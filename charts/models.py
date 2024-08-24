from django.db import models
from django.urls import reverse
from datetime import date
from django.utils import timezone
  
from datetime import timedelta  

from datetime import datetime, timedelta
from django.db.models import Sum, Count, Avg

class Workorder1(models.Model):
    
    department=models.CharField(max_length=50, default="")
    receiving_unit=models.CharField(max_length=50, default="")
    date_received=models.DateField(date.today)
    completion_date=models.DateTimeField(default=timezone.now)
    machine=models.CharField(max_length=250, default='')
    manager=models.CharField(max_length=50,blank=True, null=True, default="")
    completed=models.BooleanField(default=False)
    #completed=models.BooleanField(default=False, blank=True)
 
    def __str__(self):
        return self.department
    
    
        
    @property
    def job_completed(self):
        return self.completed=="True"
        
    @property
    def job_uncompleted(self):
        return self.completed=="False"
        
    
    
class Requisition1(models.Model):
    emanating_dept=models.CharField(max_length=200, blank = True, null = True,default='')
    requesting_officer=models.TextField('In_Charge',max_length=500, blank=True, null=True, default="")
    hod_consent=models.CharField(max_length=30, default='')
    action_by=models.CharField(max_length=200, blank = True, null = True,default='')
    manager=models.CharField(max_length=50,blank=True, null=True, default="")
    quantity=models.PositiveIntegerField()
    date_submitted=models.DateTimeField(blank=True, null=True)
    date_received=models.DateTimeField(blank=True, null=True)
    is_complete=models.BooleanField(default=False)
    request_image=models.ImageField(null=True, blank=True, upload_to="images/")
    

    def __str__(self):
       return self.emanating_dept
   
class Commodity(models.Model):
    name=models.CharField(max_length=150, default="")
    consumption_date=models.DateTimeField()
    quantity=models.FloatField()
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()

    def __str__(self):
        return self.name
    
    def commence(self):
        return self.start_date  
    
    def total_consumed(self):
        return self.quantity  
    
    def __str__(self):
        return self.end_date.strftime("%Y-%m-%d")  
    
    
   
    @classmethod
    def daily_consumption(cls, start_date, end_date):
        return cls.objects.filter(consumption_date__range=[start_date, end_date]).values('consumption_date').annotate(total=Sum('quantity'))
    
    @classmethod# 
    def average_quantity(cls):  
        return cls.objects.filter(average_consumption = Commodity.objects.annotate(  
        average_quantity=Avg('quantity')))
        
    @classmethod
    def count_commodity(cls):
        return cls.objects.filter(commodity_count = Commodity.objects.values('name').annotate(  
    total_count=Count('id')) 
)  
   
class Item(models.Model):
    name=models.CharField(max_length=500, blank=True, null=True)
    quantity=models.IntegerField(blank=True, null=True)
   

    def __str__(self):
        return self.name