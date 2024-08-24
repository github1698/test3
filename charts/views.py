from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib import messages
from .models import Requisition1, Workorder1, Commodity
from .forms import WorkorderForm1, CommodityForm
from django.core.paginator import Paginator
from django.db.models import Sum, Count, Avg
from django.utils import timezone  
from datetime import timedelta  



def add_commodity(request):
    submitted=False
    if request.method=='POST':
        form=CommodityForm(request.POST)
        if form.is_valid():
            
            commodity=form.save(commit = False)
            
    
            commodity.save()
            return HttpResponseRedirect('/add_commodity? submitted=True',{
                        "form":form})
            
    else:
        form=CommodityForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,"charts/add_energyCum.html",{"form":form,'submitted':submitted})

def commodity_consumed(request):
    commodities=Commodity.objects.all()
    thirty_days_ago = timezone.now() - timedelta(days=30)  
    total_consumed=Commodity.objects.filter(start_date__gte=thirty_days_ago).aggregate(Sum('quantity')) 
    context = {'commodities': commodities,'total_consumed': total_consumed}
    return render(request, 'charts/energy_consumed.html', context)

def commodity_consumedr(request):
    commodities=Commodity.objects.all()
    Diesel_list=Commodity.objects.filter(name='Diesel')
    Oxygen_list=Commodity.objects.filter(name='Oxygen')
    thirty_days_ago = timezone.now() - timedelta(days=30)  
    total_consumed=Commodity.objects.filter(start_date__gte=thirty_days_ago).aggregate(Sum('quantity')) 
   
    context = {'commodities': commodities,'total_consumed': total_consumed, 'Diesel_list': Diesel_list,'Oxygen_list': Oxygen_list}
    return render(request, 'myapp/dash2.html', context)

# def commodity_consumedr(request):
#     thirty_days_ago = timezone.now() - timedelta(days=30)
#     Diesel=Commodity.objects.filter(name="Diesel")
#     consumption=Commodity.objects.filter(start_date__gte=thirty_days_ago).aggregate(Sum('quantity'))
#     Oxygen=Commodity.objects.filter(name="Oxygen")
#     consumption=Commodity.objects.filter(start_date__gte=thirty_days_ago).aggregate(Sum('quantity'))
      
    #total_consumed=Commodity.objects.filter(start_date__gte=thirty_days_ago).aggregate(Sum('quantity')) 
    context = {'Diesel': Diesel,'Oxygen': Oxygen,'consumption': consumption}
    return render(request, 'myapp/dash2.html', context)


def commodity_consumption(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
                month=month.capitalize()
                month_number=list(calendar.month_name).index(month)
                month_number=int(month_number)

                cal=HTMLCalendar().formatmonth(year,month_number)
                now=datetime.now()
                current_year=now.year
                time=now.strftime('%I:%M:%S:%p')
                
                commodity_list=Commodity.objects.filter(
                      start_date__year=year,
                      start_date__month=month_number,
                      end_date__year=year,
                      end_date__month=month_number,
                )

                                       
                return render(request, "charts/energy_consumed2.html", {
        
               "year":year,
               "time":time,
               "month":month,
               "month_number":month_number,
               "cal":cal,
               "current_year":current_year,
               "commodity_list":commodity_list
        
             
                })
                
    # energy_types=Commodity.objects.all()
    # total_consumed=Commodity.daily_consumption(start_date=Commodity.start_date, end_date=Commodity.end_date)
    # average_consumed=Commodity.average_quantity()
    # context = {'energy_types': energy_types, 'total_consumed': total_consumed, 'average_consumed': average_consumed, }
    # return render(request, 'myapp/dash2.html', context)

def search_commodity(request):
    if request.method=="POST":
        searched=request.POST['searched']
        commodities=Commodity.objects.filter(requesting_unit__contains=searched)
        return render(request,"charts/search_commodity.html",{
                  "searched":searched, "commodities":commodities
            })
    
def add_workorder1(request):
    submitted=False
    if request.method=='POST':
        form=WorkorderForm1(request.POST)
        if form.is_valid():
            
            workorder1=form.save(commit = False)
           
            workorder1.save()
            #email_add(request)
            return HttpResponseRedirect('/add_workorder1? submitted=True',{
                        "form":form})
    else:
        form=WorkorderForm1
        if 'submitted' in request.GET:
            submitted=True
    return render(request,"charts/add_workorder1.html",{"form":form,'submitted':submitted})

                                         

# def daily_consumptionReport(request):  
#     daily_consumption = Commodity.objects.values('consumption_date').annotate(  
#     total_quantity=Sum('quantity')  
#     ).order_by('consumption_date')  
#     return render(request, 'daily_consumptionReport.html', {'daily_consumption': daily_consumption})
    
    
    
def show_commodity(request, commodity_id):
    commodity=Commodity.objects.get(pk=commodity_id)
    
    return render(request,"charts/show_commodity.html",{ ''
            "commodity":commodity})
    
def delete_commodity(request, commodity_id):
    commodity=Commodity.objects.get(pk=commodity_id)
    #if request.user == workorder.manager:
    commodity.delete()
    messages.success(request, ('page deleted successfully'))
    return redirect('') 

def update_commodity(request, commodity_id):
      commodity=Commodity.objects.get(pk=commodity_id)
      form=CommodityForm(request.POST or None, request.FILES or None, instance=commodity)
      if form.is_valid():
            form.save()
            return redirect('commodity_list')
      
      return render(request,"charts/update_commodity.html",{
            "commodity":commodity, "form":form
      }) 
    

    
     

      
def add_workorder1(request):
    submitted=False
    if request.method=='POST':
        form=WorkorderForm1(request.POST)
        if form.is_valid():
            
            workorder1=form.save(commit = False)
           
            workorder1.save()
            #email_add(request)
            return HttpResponseRedirect('/add_workorder1? submitted=True',{
                        "form":form})
    else:
        form=WorkorderForm1
        if 'submitted' in request.GET:
            submitted=True
    return render(request,"charts/add_workorder1.html",{"form":form,'submitted':submitted})

def show_workordere(request,workordere_id):
    workordere=Workorder1.objects.get(pk=workordere_id)
    job_completed=(Workorder1.objects.filter(completed='True')).count()
    
    job_uncompleted=(Workorder1.objects.filter(completed='False')).count()
    return render(request,"charts/show_workorder1.html",{ ''
            "workordere":workordere, 'job_completed':job_completed, 'job_uncompleted':job_uncompleted
      })  
    
def delete_workordere(request, workordere_id):
    workorder1=Workorder1.objects.get(pk=workordere_id)
    #if request.user == workorder.manager:
    workorder1.delete()
    messages.success(request, ('page deleted successfully'))
    return redirect('') 

def update_workordere(request, workordere_id):
      workorder1=Workorder1.objects.get(pk=workordere_id)
      form=WorkorderForm1(request.POST or None, request.FILES or None, instance=workorder1)
      if form.is_valid():
            form.save()
            return redirect('workorder1_list')
      
      return render(request,"charts/update_workordere.html",{
            "workorder1":workorder1, "form":form
      }) 
    

    
     

    
def workorder1(request):
    mopdno=Workorder1.objects.filter(department='MOPD').count()
    mopdno=int(mopdno) 
    print('Number of workorder from MOPD: ', mopdno)
    
    sopdno=Workorder1.objects.filter(department='SOPD').count()
    sopdno=int(sopdno) 
    print('Number of workorder from SOPD: ', sopdno)
    
    gopdno=Workorder1.objects.filter(department='GOPD').count()
    gopdno=int(gopdno) 
    print('Number of workorder from GOPD: ', gopdno)
    
    male_medno=Workorder1.objects.filter(department='Male Medical').count()
    male_medno=int(male_medno) 
    print('Number of workorder from Male Medical: ', male_medno)
    
    female_medno=Workorder1.objects.filter(department='Female Medical').count()
    female_medno=int(female_medno) 
    print('Number of workorder from Female Medical: ', female_medno)
    
    gynno=Workorder1.objects.filter(department='Gynae').count()
    gynno=int(gynno) 
    print('Number of workorder from Gynae: ', gynno)
    
    job_fininshedno=(Workorder1.objects.filter(completed='True')).count()
    
    job_unfinishedno=(Workorder1.objects.filter(completed='False')).count()
    
    department_list=['MOPD','SOPD','GOPD','Male Medical','Female Medical','Gynae']
    quantities=[mopdno,sopdno,gopdno,male_medno,female_medno,gynno]
    
    work_status=['completed', 'uncompleted']
    status_list=[job_fininshedno, job_unfinishedno]
    context={'department_list':department_list, 'quantities':quantities, 'work_status':work_status, 'status_list':status_list}
    return render(request,'myapp/dash1.html', context)
   




def all_workorders1(request):
     # supplier_list = Supplier.objects.all().order_by('name')
    workorder1_list = Workorder1.objects.all()
     
    p=Paginator(Workorder1.objects.all(), 4)
    page=request.GET.get('page')
    workorders=p.get_page(page)
    nums="a"*workorders.paginator.num_pages
    
    return render(request,'charts/workorder3_list.html', {
            "workorder1_list":workorder1_list, 'workorders':workorders, "nums":nums
      })    
def search_workorder1(request):
    if request.method=="POST":
        searched=request.POST['searched']
        workorders1=Workorder1.objects.filter(requesting_unit__contains=searched)
        return render(request,"charts/search_workorder1.html",{
                  "searched":searched, "workorders1":workorders1
            })
    
def unfinished_workorder(request):
    unfinished_workorder = Workorder1.job_uncompleted
    context = {'unfinished_workorder': unfinished_workorder}
    return render(request, 'charts/unfinished.html', context)

def finished_workorder(request):
    finished_workorder = Workorder1.job_completed
    context = {'finished_workorder': finished_workorder}
    return render(request, 'charts/finished.html', context)
     
    

                  
               
       
def requisition1(request):
    mopdno=Requisition1.objects.filter(emanating_dept='MOPD').count()
    mopdno=int(mopdno) 
    print('Number of workorder from MOPD: ', mopdno)
    
    sopdno=Requisition1.objects.filter(emanating_dept='SOPD').count()
    sopdno=int(sopdno) 
    print('Number of workorder from SOPD: ', sopdno)
    
    gopdno=Requisition1.objects.filter(emanating_dept='GOPD').count()
    gopdno=int(gopdno) 
    print('Number of workorder from GOPD: ', gopdno)
    
    male_medno=Requisition1.objects.filter(emanating_dept='Male Medical').count()
    male_medno=int(male_medno) 
    print('Number of workorder from Male Medical: ', male_medno)
    
    female_medno=Requisition1.objects.filter(emanating_dept='Female Medical').count()
    female_medno=int(female_medno) 
    print('Number of workorder from Female Medical: ', female_medno)
    
    gynno=Requisition1.objects.filter(emanating_dept='Gynae').count()
    gynno=int(gynno) 
    print('Number of workorder from Gynae: ', gynno)
    
    department_list=['MOPD','SOPD','GOPD','Male Medical','Female Medical','Gynae']
    quantities=[mopdno,sopdno,gopdno,male_medno,female_medno,gynno]
    context={'department_list':department_list, 'quantities':quantities}
    return render(request,'myapp/dash2.html', context)
    
                  
#         def get_workorder():
#             if workorder1['department']=='MOPD':
#                 mopd.append(workorder1)
#                 mopdno=mopd.count()
#                 mopdno=int(mopdno)
            
#             elif workorder1['department']=='SOPD':
#                 sopd.append(workorder1)
#                 sopdno=sopd.count()
#                 sopdno=int(sopdno)
                
#             elif workorder1['department']=='A&E':
#                 a_e.append(workorder1)
#                 a_eno=a_e.count()
#                 a_eno=int(a_eno)
            
        
            
#             elif workorder1['department']=='Gynae':
#                 male_med.append(workorder1)
#                 male_medno=male_med.count()
#                 male_medno=int(male_medno)
            
#             elif workorder1['department']=='Male Medical':
#                 gyn.append(workorder1)
#                 gynno=gyn.count()
#                 gynno=int(gynno)
            
#             elif workorder1['department']=='Female Medical':
#                 female_med.append(workorder1)
#                 female_medno=female_med.count()
#                 female_medno=int(female_medno)
#             else:
#                 print('no workorder')
#         workorder1=get_workorder('deparment')
#     department_list.append(workorder1) 

#     department_quantity=[mopdno,sopdno,a_eno,gynno,male_medno,female_medno] 
#     if form.is_valid():
#         form.save()
#     else:
#         form=WorkorderForm1()
#     return render(request,"myapp/dash1.html",{"form":form,
               
#             #    "workorder_list":workorder_list,
#             #    "workorder_quantity":workorder_quantity,
#                "department_list":department_list,
#                "department_quantity":department_quantity})
    


# def edit_usecase(request, ucid):
#    try:
#        usecase_details = Usecase.objects.filter(usecase_id=ucid)
#        context = {"usecase_details":usecase_details[0], "usecase_types": UsecaseType.objects.all(), "usecase_kpis": Kpi.objects.all()}        



#         if request.method == "POST":
#            usecase_type = request.POST['usecase_type']
#            kpi = request.POST['kpi']
#            estimated_date = request.POST['estimated_date']
#            delivery_date = request.POST['delivery_date']
#            usecase_details = Usecase.objects.get(usecase_id=ucid)
#            usecase_details.usecase_type_id=usecase_type
#            usecase_details.kpi_id=kpi
#            if estimated_date:            
#                usecase_details.estimated_date=estimated_date
#            if delivery_date:
#                usecase_details.delivery_date=delivery_date
#            usecase_details.save()
           
#            if usecase_details:
#                messages.success(request, "Usecase Data was updated successfully!")
#                return HttpResponseRedirect(reverse('usecase-details', args=[ucid]))
#            else:
#                messages.error(request, "Some Error was occurred!")
#                return HttpResponseRedirect(reverse('update-usecase', args=[ucid]))
#        return render(request, 'UpdateUsecase.html', context)
#    except Exception as e: 
#        print(e)
#        messages.error(request, "Some Error was occurred!")
#        return HttpResponseRedirect(reverse('update-usecase', args=[ucid]))     
                        
                        
            
        
       
    
    
                                  
        
   
                  
                

# # def workorder1(request):
# #     workorder1=Workorder1.objects.all()
# #     for workorder in workorder1:
# #         if workorder['department']=='MOPD':
            
# #     if request.method=='POST':
# #         form=WorkorderForm1(request.POST)
# #         if form.is_valid():
            
# #             workorder1.save()
            
            
# #     else:
# #         form=WorkorderForm1
        
# #     return render(request,"myapp/dash1.html",{"form":form,
                                              
# #                                               })
                 

             