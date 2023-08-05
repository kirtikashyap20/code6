from django.views.generic import TemplateView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#URLConf

urlpatterns =[
    # path('',views.index, name ='index'),
    # path('',TemplateView.as_view(template_name='index.html')),
    path('', views.add_task, name='add_task'),
    path('tasks/', views.tasks, name='tasks'),
    path('taskd/<str:pk>', views.task_done, name='task_done'),
    # path('', views.tasks, name='tasks'),
    path('noview/',TemplateView.as_view(template_name='404.html')),
    path('date/',TemplateView.as_view(template_name='date.html')),
    path('container_in_gate/', views.container_in_gate, name ='container_in_gate'),
    
    path('csv_ingate/', views.csv_ingate, name ='csv_ingate'),
    path('csv_ingate_search/', views.csv_ingate_search, name ='csv_ingate_search'),
    path('csv_outgate/', views.csv_outgate, name ='csv_outgate'),
    
    
    #views data
    path('container_out_gate/', views.container_out_gate, name ='container_out_gate'),
    path('container_type/', views.container_type, name ='container_type'),
    path('driver/', views.driver, name ='driver'),
    path('steamship/', views.steamship, name ='steamship'),
    path('truck/', views.truck, name ='truck'),
    path('trucking_company/', views.trucking_company, name ='trucking_company'),
    path('yard_location/', views.yard_location, name ='yard_location'),
    
    path('gate_check/', views.gate_check, name ='gate_check'),
    path('locations/', views.locations, name ='locations'),
    path('driver_records/', views.driver_records, name ='driver_records'),
    path('prepull/', views.prepull, name ='prepull'),
    path('upcoming_deliveries/', views.upcoming_deliveries, name ='upcoming_deliveries'),
    path('chassis_damage/', views.chassis_damage, name ='chassis_damage'),
    path('all_chassis_corr/', views.all_chassis_corr, name ='all_chassis_corr'),

    #search data
    path('search_container/', views.search_container, name ='search_container'),
    path('search_container_in_gate/', views.search_container_in_gate, name ='search_container_in_gate'),
    path('search_prepull/', views.search_prepull, name ='search_prepull'),
    path('search_deliveries/', views.search_deliveries, name ='search_deliveries'),
    path('search_container_out_gate/', views.search_container_out_gate, name ='search_container_out_gate'),
    path('search_company/', views.search_company, name ='search_company'),
    path('search_multiple_containers/', views.search_multiple_containers, name ='search_multiple_containers'),
    path('chassis_loc/', views.chassis_loc, name ='chassis_loc'),
    


    #add data
    path('add_steamship/', views.add_steamship, name ='add_steamship'),
    path('add_trucking_company/', views.add_trucking_company, name ='add_trucking_company'),
    path('add_driver/', views.add_driver, name ='add_driver'),
    path('add_truck/', views.add_truck, name ='add_truck'),
    path('add_container_type/', views.add_container_type, name ='add_container_type'),
    path('add_container_in_gate/', views.add_container_in_gate, name ='add_container_in_gate'),
    path('update_yard_location/<str:pk>', views.update_yard_location, name ='update_yard_location'),
    path('add_yard_location/', views.add_yard_location, name ='add_yard_location'),
    path('add_gate_check/', views.add_gate_check, name ='add_gate_check'),
    path('add_prepull/', views.add_prepull, name ='add_prepull'),
    path('add_chassis_damage/', views.add_chassis_damage, name ='add_chassis_damage'),



    #update data
    path('update_container_in_gate/<str:pk>', views.update_container_in_gate, name ='update_container_in_gate'),
    path('update_container_out_gate/<str:pk>', views.update_container_out_gate, name ='update_container_out_gate'),
    path('update_driver/<str:pk>', views.update_driver, name ='update_driver'),
    path('update_truck/<str:pk>', views.update_truck, name ='update_truck'),
    path('update_trucking_company/<str:pk>', views.update_trucking_company, name ='update_trucking_company'),
    path('update_gate_check/<str:pk>', views.update_gate_check, name ='update_gate_check'),
    path('gate_out/<str:pk>', views.gate_out, name ='gate_out'),
    path('update_prepull/<str:pk>', views.update_prepull, name ='update_prepull'),
    path('update_chassis_damage/<str:pk>', views.update_chassis_damage, name ='update_chassis_damage'),
    path('in_gate/<str:pk>', views.in_gate, name ='in_gate'),
    path('chassis_corr/<str:pk>', views.chassis_corr, name ='chassis_corr'),
    path('update_chassis_corr/<str:pk>', views.update_chassis_corr, name ='update_chassis_corr'),


    path('view_prepull/', views.view_prepull, name ='view_prepull'),
    path('update_view_prepull/<str:pk>', views.update_view_prepull, name ='update_view_prepull'),



    #delete data
    path('delete_container_in_gate/<str:pk>', views.delete_container_in_gate, name ='delete_container_in_gate'),
    path('delete_container_out_gate/<str:pk>', views.delete_container_out_gate, name ='delete_container_out_gate'),
    path('delete_container_type/<str:pk>', views.delete_container_type, name ='delete_container_type'),
    path('delete_driver/<str:pk>', views.delete_driver, name ='delete_driver'),
    path('delete_steamship/<str:pk>', views.delete_steamship, name ='delete_steamship'),
    path('delete_truck/<str:pk>', views.delete_truck, name ='delete_truck'),
    path('delete_trucking_company/<str:pk>', views.delete_trucking_company, name ='delete_trucking_company'),
    path('delete_yard_location/<str:pk>', views.delete_yard_location, name ='delete_yard_location'),
    path('delete_gate_check/<str:pk>', views.delete_gate_check, name ='delete_gate_check'),
    path('delete_chassis_damage/<str:pk>', views.delete_chassis_damage, name ='delete_chassis_damage'),
    path('delete_chassis_corr/<str:pk>', views.delete_chassis_corr, name ='delete_chassis_corr'),
    path('delete_prepull/<str:pk>', views.delete_prepull, name ='delete_prepull'),
    


    #detail Page
    path('detail_container_in_gate/<str:pk>', views.detail_container_in_gate, name ='detail_container_in_gate'),
    path('detail_container_out_gate/<str:pk>', views.detail_container_out_gate, name ='detail_container_out_gate'),
    path('detail_yard_location/<str:pk>', views.detail_yard_location, name ='detail_yard_location'),
    path('detail_gate_check/<str:pk>', views.detail_gate_check, name ='detail_gate_check'),
    path('detail_trucking_company/<str:company_name>', views.detail_trucking_company, name ='detail_trucking_company'),



    #other changelist
    path('multiple_locations/', views.multiple_locations, name ='multiple_locations'),
    path('multiple_search_locations/', views.multiple_search_locations, name ='multiple_search_locations'),
    
    path('ml_inbound_dt/', views.ml_inbound_dt, name ='ml_inbound_dt'),
    

    ]