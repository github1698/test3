from django.urls import path
from .import views

urlpatterns = [
    path('requisition_1',views.requisition1,name='requisition-1'),
    path('workorder_1',views.workorder1,name='workorder-1'),
    path('all_workorders1',views.all_workorders1,name='workorder1_list'),
    path('show_workordere/<workordere_id>', views.show_workordere, name='show-workordere'),
    path('update_workordere/<workordere_id>', views.update_workordere, name='update-workordere'),
    path('search_workorder1',views.search_workorder1,name='search-workorder1'),
    path('add_workorder1',views.add_workorder1,name='add-workorder1'),
    path('delete_workordere/<workordere_id>',views.delete_workordere,name='delete-workordere'),
    path('commodity_consumedr',views.commodity_consumedr,name='commodity-consumedr'),
    path('commodity_consumed',views.commodity_consumed,name='commodity-consumed'),
    #path('daily_consumptionReport',views.daily_consumptionReport,name='daily-consumptionReport'),
    path('add_commodity',views.add_commodity,name='add-commodity'),
    path('commodity_consumption',views.commodity_consumption,name='commodity-consumption'),
    path('search_commodity',views.search_commodity,name='search-commodity'),
    path('show_commodity/<commodity_id>', views.show_commodity, name='show-commodity'),
    path('update_commodity/<commodity_id>', views.update_commodity, name='update-commodity'),
    path('search_commodity',views.search_commodity,name='search-commodity'),
   # path('add_workorder1',views.add_workorder1,name='add-workorder1'),
]

