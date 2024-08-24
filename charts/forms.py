from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Requisition1, Workorder1, Commodity

class WorkorderForm1(forms.ModelForm):
    class Meta:
        model=Workorder1
        fields='__all__'
        labels={
            
            'department':'',
            'receiving_unit':'',
            'date_received':'',
            'completion_date':'',
            'machine':'',
            'attendees':'',
            'completed':'',
        

        }
        widgets = {
            
            'department':forms.TextInput(attrs={'class':'form-control','placeholder':'Department'}),
            'receiving_unit':forms.TextInput(attrs={'class':'form-control','placeholder':'Receiving Unit'}),
            'date_received':forms.DateInput(attrs={'class':'form-control','placeholder':'Received Date YYYY-MM-DD'}),
            'completion_date':forms.DateInput(attrs={'class':'form-control','placeholder':'Completion Date YYYY-MM-DD'}),
            'machine':forms.TextInput(attrs={'class':'form-control','placeholder':'machines'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attending Officer'}),
            'complete':forms.BooleanField(required=False)
        }
class RequisitionForm(ModelForm):
    is_complete=forms.BooleanField(required=True)
    class Meta:
        model=Requisition1
        fields=('emanating_dept','requesting_officer','hod_consent','action_by','manager','date_submitted','date_received','is_complete')
        labels={
            'emanating_dept':'',
           
            'requesting_officer':' ',
            'hod_consent':'',
           
           
            'action_by':'',
    
            'manager':'Manager',
           
            'date_submitted':'YYYY-MM-DD',
            'date_received':'',
            'is_complete':'',
           
            

        }
        widgets = {
            'emanating_dept':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Requesting Department'}),
            'requesting_officer':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Requesting Officer'}),
            'hod_consent':forms.TextInput(attrs={'class':'form-control','placeholder':'HOD Comment'}),
                        
            'equipment':forms.Select(attrs={'class':'form-control','placeholder':'Equipment Type'}),
            'action_by':forms.TextInput(attrs={'class':'form-control','placeholder':'Supervisor'}),
            'section':forms.Select(attrs={'class':'form-control','placeholder':'Section'}),
            
            'date_submitted':forms.TextInput(attrs={'class':'form-control','placeholder':'Date Submitted'}),
            'date_received':forms.TextInput(attrs={'class':'form-control','placeholder':'Date Received'}),
            'is_complete':forms.BooleanField(),
            
                }

class CommodityForm(ModelForm):
    class Meta:
        model=Commodity
        fields=('name','consumption_date','quantity','start_date','end_date')
        labels={
            'name':'',
            'consumption_date':' ',
            'quantity':'',
            'start_date':'',
            'end_date':'',
           
           
           
           
            

        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Commodity name'}),
            'consumption_date':forms.DateTimeInput(attrs={'type': 'datetime-local','input_formats':'%Y-%m-%dT%H:%M'}), 
            'quantity':forms.TextInput(attrs={'class':'form-control','placeholder':'Quantity'}),
            'start_date':forms.DateTimeInput(attrs={'type': 'datetime-local','input_formats':'%Y-%m-%dT%H:%M'}),  
        
    
            'end_date':forms.DateTimeInput(attrs={'type': 'datetime-local','input_formats':'%Y-%m-%dT%H:%M'}),  
        
            
                }

