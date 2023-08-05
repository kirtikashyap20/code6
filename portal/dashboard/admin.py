from django.db.models.aggregates import Count
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models
# Register your models here.


@admin.register(models.Chassis_Corr)
class Chassis_CorrAdmin(admin.ModelAdmin):
    list_display = ['chassis_number']



@admin.register(models.Chassis_Damage)
class Chassis_DamageAdmin(admin.ModelAdmin):
    list_display = ['chassis_number','dmg_img']



@admin.register(models.Yard_location)
class Yard_locationAdmin(admin.ModelAdmin):
    list_display = ['user','location']
    search_fields = ['location__istartswith']
    list_filter = ['location']
    


@admin.register(models.ContainerType)
class ContainerTypeAdmin(admin.ModelAdmin):
    # list_display = ['containerTypeAndSize', 'container_in_gate_count']

    list_display = ['user','containerTypeAndSize']
    search_fields = ['containerTypeAndSize__istartswith']
    list_filter = ['containerTypeAndSize']
    
    # def container_in_gate_count(self,ContainerType):
    #     url = (
    #         reverse('admin:Dashboard_container_in_gate_changelist')
    #         + '?'
    #         + urlencode({
    #             'containerType__id': str(ContainerType.id)
    #         })
    #     )
    #     return format_html('<a href="{}">{}</a>', url, ContainerType.container_in_gate_count)
        

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            container_in_gate_count = Count('container_in_gate')
        )
    
    


@admin.register(models.Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['user','driver_name','license_number']
    list_per_page = 20
    search_fields=['driver_name__istartswith','license_number__istartswith']


@admin.register(models.TruckingCompany)
class TruckingCompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name','company_phone','company_email','company_address', 'user','container_in_gate_count']
    list_per_page = 20
    search_fields = ['company_name__istartswith']

    def container_in_gate_count(self,TruckingCompany):
        url = (
            reverse('admin:Dashboard_container_in_gate_changelist')
            + '?'
            + urlencode({
                'containerCompanyType__id': str(TruckingCompany.id)
            })
        )
        return format_html('<a href="{}">{}</a>', url, TruckingCompany.container_in_gate_count)
        

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            container_in_gate_count = Count('container_in_gate')
        )


@admin.register(models.Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ['driver','unit_number','vin','plate_number','year','make','added_on','user']
    list_per_page = 20
    list_filter = ['vin','unit_number','year','added_on']
    search_fields = ['driver__istartswith','unit_number__istartswith','vin__istartswith','plate_number__istartswith']


@admin.register(models.Steamship)
class SteamshipAdmin(admin.ModelAdmin):
    list_display =['user','shipping_name','container_in_gate_Steamship_count']
    list_per_page = 20
    search_fields = ['shipping_name__istartswith']
    
    def container_in_gate_Steamship_count(self,Steamship):
        url = (
            reverse('admin:Dashboard_container_in_gate_changelist')
            + '?'
            + urlencode({
                'container_Steamship__id': str(Steamship.id)
            })
        )
        return format_html('<a href="{}">{}</a>', url, Steamship.container_in_gate_Steamship_count)
        

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            container_in_gate_Steamship_count = Count('container_in_gate')
        )
    



@admin.register(models.Container_in_gate)
class Container_in_gateAdmin(admin.ModelAdmin):
    #list_display = [f.container_number for f in Container_in_gate._meta.fields]
    # list_display = ['user','container_number','containerType','container_plug_check','yard_location','container_status','booking_number','seal_number','created_on','delivery_date','destination','weight','weight_type','steamshiping_line','trucking_company','container_company','container_company_manual','truck_number_in','manual_truck_number_in','chassis_number']
    # autocomplete_fields = ['containerType','steamshiping_line','container_company','truck_number_in']
    #list_editable = ['']
    #readonly_fields = ['user_detail']
    list_per_page = 20
    # list_filter = ['container_company','trucking_company']
    # search_feilds = ['container_number__istartswith','containerType__istartswith','container_plug_check__istartswith','yard_location__istartswith','container_status__istartswith','booking_number__istartswith','seal_number__istartswith','created_on__istartswith','destination__istartswith','weight__istartswith','steamshiping_line__istartswith','container_company__istartswith','truck_number__istartswith','chassis_number__istartswith','damange_check__istartswith','chassis_damage__istartswith']

@admin.register(models.Gatecheck)
class GatecheckAdmin(admin.ModelAdmin):
    # list_display = ['type','trucking_company_gate','outer_company_gate','outer_company_manual_gate','truck_number_gate','manual_truck_number_gate','chassis_number','comments','user']
    # autocomplete_fields = ['outer_company_gate','truck_number_gate']
    list_per_page = 20
    


@admin.register(models.Container_gate_out)
class Container_gate_outAdmin(admin.ModelAdmin):

    # list_display = ['user','container_number','containerType','container_plug_check','yard_location','container_status','booking_number','seal_number','enter_date','delivery_date','destination','weight','weight_type','steamshiping_line','trucking_company_in','container_company_in','container_company_manual_in','truck_number_in','manual_truck_number_in','chassis_number_in','special_notes_in', 'trucking_company_out', 'outer_company_out','company_manual_out','truck_number_out','manual_truck_number_out', 'chassis_number_out','comments','in_gate_user','total_days']
    # autocomplete_fields = ['outer_company_out','truck_number_out']
    list_per_page = 20
    # list_filter = ['outer_company_out']
    # search_feilds = ['chassis_number_out__istartswith']
        



@admin.register(models.Prepull)
class PrepullAdmin(admin.ModelAdmin):
    list_display = ['user','container_number','steamshiping_line','created_on','delivery_date','destination','weight','weight_type','comments']
    autocomplete_fields = ['steamshiping_line']
    list_per_page = 20
    search_feilds = ['container_number__istartswith','created_on__istartswith','destination__istartswith','weight__istartswith']
