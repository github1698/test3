from django.contrib import admin
from . models import Requisition1,  Workorder1, Commodity, Item

@admin.register(Requisition1)
class RequisitionAdmin(admin.ModelAdmin):
    list_display=('emanating_dept','quantity')
    ordering=('emanating_dept',)
    search_fields=('emanating_dept','quantity')


@admin.register(Workorder1)
class Workorder1Admin(admin.ModelAdmin):
    list_display=('department','date_received','completed')
    ordering=('department',)
    search_fields=('department','completed')
    
@admin.register(Commodity)
class CommodityAdmin(admin.ModelAdmin):
    list_display=('name','quantity','total_consumed')
    ordering=('name',)
    search_fields=('name','consumption_date')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=('name','quantity')
    ordering=('name',)
    search_fields=('name','quantity')
    