# authentication/views.py
from dataclasses import fields
import datetime
from operator import add
from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render

from dashboard.decorators import allowed_user
from . import models
from datetime import date, timezone
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Add_Gatecheck, Add_Yard_Location, Add_Container_Type, Add_Driver, Add_Steamship, Add_Truck, Add_Trucking_Company, Add_Container_In_Gate, Add_Container_Gate_Out, Add_Prepull, Add_Prepull_test, Update_Container_Out_Gate
from dashboard.models import Yard_location, ContainerType, Container_in_gate, Container_gate_out, Driver, TruckingCompany, Truck, Steamship, Gatecheck, Prepull
import csv
from django.utils.encoding import smart_str

from django.contrib.auth.decorators import login_required
from .filters import *
from django.db.models import Count, Max
import datetime
from itertools import chain

from django.db.models import Q
from django.forms import modelformset_factory, inlineformset_factory, formset_factory

from django.db.models import Q
from django.db.models import Sum
from authentication.models import Tasks
from authentication.forms import Add_Task

from django.http import JsonResponse
from django.core import serializers


def csv_ingate(request):
	# response content type
	response = HttpResponse(content_type='text/csv')
	#decide the file name
	response['Content-Disposition'] = 'attachment; filename="container_in_gate.csv"'

	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8'))

	#write the headers
	writer.writerow([
		smart_str(u"Enter Date"),
        smart_str(u"Yard Loc"),
		smart_str(u"Container No."),
        smart_str(u"Cont. Type"),
		smart_str(u"Delivery Date"),
		smart_str(u"Load/Empty"),
        smart_str(u"Destination"),
        smart_str(u"Weight"),
        smart_str(u"Steamship"),
        smart_str(u"Trucking Company"),
        smart_str(u"Truck Number"),
        smart_str(u"Notes"),
        smart_str(u"Chassis Number"),
	])
	#get data from database or from text file....
	events = Container_in_gate.objects.all()
    #dummy function to fetch data
	for event in events:
		writer.writerow([
			smart_str(event.created_on.strftime("%b %d, %I:%M %p")),
            smart_str(event.yard_location),
            smart_str(event.container_number),
            smart_str(event.containerType),
            smart_str(event.delivery_date),
			smart_str(event.container_status),
			smart_str(event.destination),
			smart_str(event.weight),
            smart_str(event.steamshiping_line),
            smart_str(event.trucking_company),
            smart_str(event.truck_number),
            smart_str(event.comments),
            smart_str(event.chassis_number),
		])
	return response



def csv_ingate_search(request):
	# response content type
	response = HttpResponse(content_type='text/csv')
	#decide the file name
	response['Content-Disposition'] = 'attachment; filename="container_in_gate.csv"'

	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8'))

	#write the headers
	writer.writerow([
		smart_str(u"Enter Date"),
        smart_str(u"Yard Loc"),
		smart_str(u"Container No."),
        smart_str(u"Cont. Type"),
		smart_str(u"Delivery Date"),
		smart_str(u"Load/Empty"),
        smart_str(u"Destination"),
        smart_str(u"Weight"),
        smart_str(u"Steamship"),
        smart_str(u"Trucking Company"),
        smart_str(u"Truck Number"),
        smart_str(u"Notes"),
        smart_str(u"Chassis Number"),
	])
	#get data from database or from text file....
	events = search_container_in_gate
    #dummy function to fetch data
	for event in events:
		writer.writerow([
			smart_str(event.created_on.strftime("%b %d, %I:%M %p")),
            smart_str(event.yard_location),
            smart_str(event.container_number),
            smart_str(event.containerType),
            smart_str(event.delivery_date),
			smart_str(event.container_status),
			smart_str(event.destination),
			smart_str(event.weight),
            smart_str(event.steamshiping_line),
            smart_str(event.trucking_company),
            smart_str(event.truck_number),
            smart_str(event.comments),
            smart_str(event.chassis_number),
		])
	return response




def csv_outgate(request):
	# response content type
	response = HttpResponse(content_type='text/csv')
	#decide the file name
	response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.csv"'

	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8'))

	#write the headers
	writer.writerow([
		smart_str(u"Event Name"),
		smart_str(u"Start Date"),
		smart_str(u"End Date"),
		smart_str(u"Notes"),
	])
	#get data from database or from text file....
	events = Container_gate_out.objects.all()
     #dummy function to fetch data
	for event in events:
		writer.writerow([
			smart_str(event.container_number),
			smart_str(event.created_on),
			smart_str(event.containerType),
			smart_str(event.comments),
		])
	return response




@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def add_task(request):
    query_set = Tasks.objects.order_by('-created_on')
    if request.method == 'POST':
        form = Add_Task(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.status= 'pending'
            form = form.save()
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponseRedirect('/container_in_gate/')
    else:
        form = Add_Task()
        

    return render(request, 'index.html', {'form': form, 'tasks': list(query_set)})





@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def tasks(request):
    query_set = Tasks.objects.order_by('-created_on')
    return render(request, 'dashboard/output/tasks.html', {'tasks': list(query_set)})





@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def task_done(request,pk):
    query_set = Tasks.objects.order_by('-created_on')
    return render(request, 'dashboard/output/tasks.html', {'tasks': list(query_set)})







@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def view_prepull(request):
    data = Prepull.objects.all()
    PrepullFormSet = modelformset_factory(Prepull, form=Add_Prepull_test)
    if request.method == 'POST':
        formset = PrepullFormSet(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = PrepullFormSet()
    return render(request, 'dashboard/output/test.html', {'formset':formset})





#driver Information
@login_required
@allowed_user(allowed_roles=['admin'])
def driver(request):
    query_set = Driver.objects.all()
    return render(request, 'dashboard/output/driver.html', {'driver': list(query_set)}) 


@login_required
@allowed_user(allowed_roles=['admin'])
def add_driver(request):
    if request.method == 'POST':
        add_driver = Add_Driver(request.POST)
        if add_driver.is_valid():
            add_driver = add_driver.save(commit=False)
            add_driver.user= request.user
            add_driver = add_driver.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        add_driver = Add_Driver()

    return render(request, 'dashboard/input/add_driver.html', {'add_driver': add_driver})

@login_required
@allowed_user(allowed_roles=['admin'])
def update_driver(request, pk):
    data = Driver.objects.get(id=pk)
    add_driver = Add_Driver(instance = data)

    if request.method == 'POST':
        add_driver = Add_Driver(request.POST, instance=data)
        if add_driver.is_valid():
            add_driver = add_driver.save()
            return HttpResponseRedirect('/dashboard/driver/')

    return render(request, 'dashboard/input/add_driver.html', {'add_driver': add_driver})


@login_required
@allowed_user(allowed_roles=['admin'])
def delete_driver(request, pk):
    data = Driver.objects.get(id=pk)

    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/dashboard/driver/')

    return render(request, 'dashboard/delete/driver.html', {'data': data})


# *****************************************************************************

#truck information
@login_required
@allowed_user(allowed_roles=['admin'])
def truck(request):
    query_set = Truck.objects.all()
    return render(request, 'dashboard/output/truck.html', {'truck': list(query_set)})



@login_required
@allowed_user(allowed_roles=['admin'])
def add_truck(request):
    if request.method == 'POST':
        add_truck = Add_Truck(request.POST)
        if add_truck.is_valid():
            add_truck = add_truck.save(commit=False)
            add_truck.user= request.user
            add_truck = add_truck.save()
            return HttpResponseRedirect('/dashboard/truck/')
    else:
        add_truck = Add_Truck()

    return render(request, 'dashboard/input/add_truck.html', {'add_truck': add_truck})


@login_required
@allowed_user(allowed_roles=['admin'])
def update_truck(request, pk):
    data = Truck.objects.get(id=pk)
    add_truck = Add_Truck(instance = data)

    if request.method == 'POST':
        add_truck = Add_Truck(request.POST, instance=data)
        if add_truck.is_valid():
            add_truck = add_truck.save()
            return HttpResponseRedirect('/dashboard/truck/')

    return render(request, 'dashboard/input/add_truck.html', {'add_truck': add_truck})


@login_required
@allowed_user(allowed_roles=['admin'])
def delete_truck(request, pk):
    data = Truck.objects.get(id=pk)

    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/dashboard/truck/')

    return render(request, 'dashboard/delete/truck.html', {'data': data})




#********************************************************************
#trucking Company

@login_required
@allowed_user(allowed_roles=['admin'])
def trucking_company(request):
    query_set = TruckingCompany.objects.all()
    return render(request, 'dashboard/output/trucking_company.html', {'trucking_company': list(query_set)})



@login_required
@allowed_user(allowed_roles=['admin'])
def add_trucking_company(request):
    if request.method == 'POST':
        add_trucking_company = Add_Trucking_Company(request.POST)
        if add_trucking_company.is_valid():
            add_trucking_company = add_trucking_company.save(commit=False)
            add_trucking_company.user= request.user
            add_trucking_company = add_trucking_company.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        add_trucking_company = Add_Trucking_Company()

    return render(request, 'dashboard/input/add_trucking_company.html', {'add_trucking_company': add_trucking_company})



@login_required
@allowed_user(allowed_roles=['admin'])
def update_trucking_company(request, pk):
    data = TruckingCompany.objects.get(id=pk)
    add_trucking_company = Add_Trucking_Company(instance = data)

    if request.method == 'POST':
        add_trucking_company = Add_Trucking_Company(request.POST, instance=data)
        if add_trucking_company.is_valid():
            add_trucking_company = add_trucking_company.save()
            return HttpResponseRedirect('/dashboard/')

    return render(request, 'dashboard/input/add_trucking_company.html', {'add_trucking_company': add_trucking_company})


@login_required
@allowed_user(allowed_roles=['admin'])
def delete_trucking_company(request, pk):
    data = TruckingCompany.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/dashboard/trucking_company/')

    return render(request, 'dashboard/delete/trucking_company.html', {'data': data})




@login_required
@allowed_user(allowed_roles=['admin','dispatch'])
def detail_trucking_company(request, company_name):
    data = Container_gate_out.objects.filter(outer_company_in__iexact=company_name)
    company_name = company_name
    amount = data.aggregate(Sum('invoice'))
    return render(request, 'dashboard/detail/trucking_company.html', {'data': list(data), 'company_name': company_name, 'amount': amount})


@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def search_company(request):
    if request.method == 'GET':
        qs = Container_gate_out.objects.all()
        company_name= request.GET.get('company_name')
        ofrom= request.GET.get('ofrom')
        oto= request.GET.get('oto')
        submitbutton= request.GET.get('submit')
        if company_name != '':
            qs = qs.filter(outer_company__icontains=company_name)
        if ofrom != '':
            qs = qs.filter(created_on__gte=ofrom)
        if oto != '' :
            qs = qs.filter(created_on__lt = oto)

        qs = qs.order_by('-created_on')
        amount = qs.aggregate(Sum('invoice'))
        
        context={'results': list(qs),
                     'submitbutton': submitbutton, 
                     'company_name':company_name,
                     'amount': amount
                }
        return render(request, 'dashboard/detail/trucking_company.html', context)
    else:
        return render(request, 'dashboard/detail/trucking_company.html')



#***********************************************************************
#container_in_gate 


@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def locations(request):
    # locations = Container_in_gate.objects.values('yard_location').annotate(number_of_entries=Count('yard_location'))
    locations = Container_in_gate.objects.values('yard_location').distinct()
    print(locations)
    containers_l = Container_in_gate.objects.all()[:10]
    return render(request, 'dashboard/output/locations.html', {'locations': list(locations), 'contianers':list(containers_l)})


@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def update_yard_location(request, pk):
    data = Container_in_gate.objects.get(id=pk)
    update_yard_location = Add_yl(instance = data)
    if request.method == 'POST':
        update_yard_location = Add_yl(request.POST, instance=data)
        if update_yard_location.is_valid():
            update_yard_location = update_yard_location.save()
            return HttpResponseRedirect('/dashboard/container_in_gate/')

    return render(request, 'dashboard/input/add_yard_location.html', {'update_yard_location': update_yard_location})




@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def container_in_gate(request):
    query_set = Container_in_gate.objects.order_by('-created_on')[:50]
    today = datetime.date.today()
    container_type= ContainerType.objects.all()
    shipping_name= Steamship.objects.all()
    count = Container_in_gate.objects.count()
    return render(request, 'dashboard/output/container_in_gate.html', {'container_ingate': list(query_set), 'in_count': count,'shipping_name':list(shipping_name), 'container_type':list(container_type)})




@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def add_container_in_gate(request):    
    err=" "
    if request.method == 'POST':
        add_container_in_gate = Add_Container_In_Gate(request.POST)
        if add_container_in_gate.is_valid():
            add_container_in_gate = add_container_in_gate.save(commit=False)
            add_container_in_gate.user= request.user
            data = add_container_in_gate
            b = Gatecheck(
                type = 'IN',
                created_on = data.created_on,
                container_number = data.container_number,
                trucking_company = data.trucking_company,
                outer_company = data.outer_company,
                truck_number = data.truck_number,
                manual_truck_number = data.manual_truck_number,
                chassis_number = data.chassis_number,
                comments = data.comments,
                user = data.user
            )
            b.save()

            if not Container_in_gate.objects.filter(container_number=add_container_in_gate.container_number).exists():
                if not Prepull.objects.filter(container_number=add_container_in_gate.container_number).exists():
                    err="Container ingated"
                    add_container_in_gate = add_container_in_gate.save()
                    return HttpResponseRedirect('/dashboard/container_in_gate')
                else:
                    err= "container present in prepull"
                    add_container_in_gate = Add_Container_In_Gate()
                    return render(request, 'dashboard/input/add_container_in_gate.html', {'add_container_in_gate': add_container_in_gate,'err':err})   
            else:
                err= "container already in-gated"
                add_container_in_gate = Add_Container_In_Gate()
                return render(request, 'dashboard/input/add_container_in_gate.html', {'add_container_in_gate': add_container_in_gate,'err':err})
    else:
        add_container_in_gate = Add_Container_In_Gate()
    return render(request, 'dashboard/input/add_container_in_gate.html', {'add_container_in_gate': add_container_in_gate,'err':err})



# @login_required
# @allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
# def add_container_in_gate(request):    
#     err=" "
#     if request.is_ajax and request.method == "POST":
#         add_container_in_gate = Add_Container_In_Gate(request.POST)
#         if add_container_in_gate.is_valid():
#             add_container_in_gate = add_container_in_gate.save(commit=False)
#             add_container_in_gate.user= request.user
#             data = add_container_in_gate
#             b = Gatecheck(
#                 type = 'IN',
#                 created_on = data.created_on,
#                 container_number = data.container_number,
#                 trucking_company = data.trucking_company,
#                 outer_company = data.outer_company,
#                 truck_number = data.truck_number,
#                 manual_truck_number = data.manual_truck_number,
#                 chassis_number = data.chassis_number,
#                 comments = data.comments,
#                 user = data.user
#             )
#             b.save()

#             if not Container_in_gate.objects.filter(container_number=add_container_in_gate.container_number).exists():
#                 err="Container ingated"
#                 add_container_in_gate = add_container_in_gate.save()
#                 ser_instance = serializers.serialize('json', [ add_container_in_gate, ])
#                 # send to client side.
#                 return JsonResponse({"instance": ser_instance}, status=200)
#             else:
#                 err= "container already in-gated"
#                 add_container_in_gate = Add_Container_In_Gate()
#                 return render(request, 'dashboard/input/add_container_in_gate.html', {'add_container_in_gate': add_container_in_gate,'err':err})
#     else:
#         add_container_in_gate = Add_Container_In_Gate()
#         return JsonResponse({"error": add_container_in_gate.errors}, status=400)
#     return JsonResponse({"error": ""}, status=400)

@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def update_container_in_gate(request, pk):
    data = Container_in_gate.objects.get(id=pk)
    add_container_in_gate = Add_Container_In_Gate(instance = data)

    if request.method == 'POST':
        add_container_in_gate = Add_Container_In_Gate(request.POST, instance=data)
        if add_container_in_gate.is_valid():
            add_container_in_gate = add_container_in_gate.save()
            return HttpResponseRedirect('/dashboard/container_in_gate/')
    return render(request, 'dashboard/input/add_container_in_gate.html', {'add_container_in_gate': add_container_in_gate})


@login_required
@allowed_user(allowed_roles=['admin'])
def delete_container_in_gate(request, pk):
    data = Container_in_gate.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/dashboard/container_in_gate/')
    return render(request, 'dashboard/delete/container_in_gate.html', {'data': data})


@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def detail_container_in_gate(request, pk):
    data = Container_in_gate.objects.get(id=pk)
    return render(request, 'dashboard/detail/container_in_gate.html', {'data': data})





#**********************************************************************************
#container Type

@login_required
@allowed_user(allowed_roles=['admin'])
def container_type(request):
    query_set = ContainerType.objects.all()
    return render(request, 'dashboard/output/container_type.html', {'container_type': list(query_set)}) 



@login_required
@allowed_user(allowed_roles=['admin'])
def add_container_type(request):
    if request.method == 'POST':
        add_container_type = Add_Container_Type(request.POST)
        if add_container_type.is_valid():
            fs = add_container_type.save(commit=False)
            fs.user= request.user
            add_container_type = add_container_type.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        add_container_type = Add_Container_Type()
    return render(request, 'dashboard/input/add_container_type.html', {'add_container_type': add_container_type})




@login_required
@allowed_user(allowed_roles=['admin'])
def delete_container_type(request, pk):
    data = ContainerType.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/dashboard/container_type/')
    return render(request, 'dashboard/delete/container_type.html', {'data': data})


#*************************************************************************
#steamship

@login_required
@allowed_user(allowed_roles=['admin'])
def steamship(request):
    query_set = Steamship.objects.all()
    return render(request, 'dashboard/output/steamship.html', {'steamship': list(query_set)}) 


@login_required
@allowed_user(allowed_roles=['admin'])
def add_steamship(request):
    if request.method == 'POST':
        add_steamship = Add_Steamship(request.POST)
        if add_steamship.is_valid():
            add_steamship = add_steamship.save(commit=False)
            add_steamship.user= request.user
            add_steamship = add_steamship.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        add_steamship = Add_Steamship()
    return render(request, 'dashboard/input/add_steamship.html', {'add_steamship': add_steamship})




@login_required
@allowed_user(allowed_roles=['admin'])
def delete_steamship(request, pk):
    data = Steamship.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/dashboard/steamship/')
    return render(request, 'dashboard/delete/steamship.html', {'data': data})





#********************************************************************
# yard location


@login_required
@allowed_user(allowed_roles=['admin'])
def yard_location(request):
    query_set = Yard_location.objects.all()
    return render(request, 'dashboard/output/yard_location.html', {'yard_location': list(query_set)})


@login_required
@allowed_user(allowed_roles=['admin'])
def add_yard_location(request):
    if request.method == 'POST':
        add_yard_location = Container_in_gate(request.POST)
        if add_yard_location.is_valid():
            add_yard_location = add_yard_location.save(commit=False)
            add_yard_location.user= request.user
            add_yard_location = add_yard_location.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        add_yard_location = Add_Yard_Location()
    return render(request, 'dashboard/input/add_yard_location.html', {'add_yard_location': add_yard_location})




@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def update_yard_location(request, pk):
    data = Container_in_gate.objects.get(id=pk)
    update_yard_location = Add_yl(instance = data)
    if request.method == 'POST':
        update_yard_location = Add_yl(request.POST, instance=data)
        if update_yard_location.is_valid():
            update_yard_location = update_yard_location.save()
            return HttpResponseRedirect('/dashboard/container_in_gate/')
    return render(request, 'dashboard/input/add_yard_location.html', {'update_yard_location': update_yard_location})



@login_required
@allowed_user(allowed_roles=['admin'])
def delete_yard_location(request, pk):
    data = Yard_location.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/dashboard/yard_location/')
    return render(request, 'dashboard/delete/yard_location.html', {'data': data})


@login_required
@allowed_user(allowed_roles=['admin'])
def detail_yard_location(request, pk):
    data = Yard_location.objects.get(id=pk)
    return render(request, 'dashboard/detail/yard_location.html', {'data': data})




#********************************************************************
# Gate Check



@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def gate_check(request):
    query_set = Gatecheck.objects.all()
    container_in_gate_queryset = Container_in_gate.objects.all()
    container_out_gate_queryset = Container_gate_out.objects.all()
    merged = sorted(chain(query_set, container_out_gate_queryset), key=lambda instance: instance.created_on, reverse=True)[:200]
    return render(request, 'dashboard/output/gate_check.html', {'gate_check': list(query_set), 'in_gate': list(container_in_gate_queryset), 'out_gate': list(container_out_gate_queryset), 'merged' : merged})

 
@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def add_gate_check(request):
    if request.method == 'POST':
        add_gate_check = Add_Gatecheck(request.POST)
        if add_gate_check.is_valid():
            add_gate_check = add_gate_check.save(commit=False)
            add_gate_check.user= request.user
            add_gate_check = add_gate_check.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        add_gate_check = Add_Gatecheck()

    return render(request, 'dashboard/input/add_gate_check.html', {'add_gate_check': add_gate_check})


@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def update_gate_check(request, pk):
    data = Gatecheck.objects.get(id=pk)
    add_gate_check = Add_Gatecheck(instance = data)
    if request.method == 'POST':
        add_gate_check = Add_Gatecheck(request.POST, instance=data)
        if add_gate_check.is_valid():
            add_gate_check = add_gate_check.save()
            return HttpResponseRedirect('/dashboard/gate_check/')
    return render(request, 'dashboard/input/add_gate_check.html', {'add_gate_check': add_gate_check})


@login_required
@allowed_user(allowed_roles=['admin'])
def delete_gate_check(request, pk):
    data = Gatecheck.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/dashboard/gate_check/')

    
@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def detail_gate_check(request, pk):
    data = Gatecheck.objects.get(id=pk)
    return render(request, 'dashboard/detail/gate_check.html', {'data': data})





#********************************************************************
# Driver records



def driver_records(request):
    if request.method == 'GET':
        query= request.GET.get('container_number')
        submitbutton= request.GET.get('submit')
        if query is not None:
            results= Container_in_gate.objects.values("container_number","yard_location").filter(container_number__iexact=query).distinct()
            cont = Container_in_gate.objects.values("container_number","yard_location").filter(container_number__icontains=query)
            context={'results': results,
                    'cont':list(cont),
                    'submitbutton': submitbutton}
            return render(request, 'dashboard/driver_records.html', context)
        else:
            return render(request, 'dashboard/driver_records.html')
    else:
        return render(request, 'dashboard/driver_records.html')









#********************************************************************
# Search Filter


@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def search_container(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            prepull_queryset = Prepull.objects.filter(container_number__icontains=query)
            container_in_gate_queryset = Container_in_gate.objects.filter(container_number__iexact=query)
            container_out_gate_queryset = Container_gate_out.objects.filter(container_number__iexact=query)
            if prepull_queryset:
                results= prepull_queryset.distinct()
                status = "prepull"
            elif not container_in_gate_queryset:
                results= container_out_gate_queryset.distinct()
                status = "outgate"
            else:
                results= container_in_gate_queryset.distinct()
                status = "ingate"
            

            merged = sorted(chain(prepull_queryset, container_in_gate_queryset, container_out_gate_queryset), key=lambda instance: instance.created_on, reverse=True)
            
            context={'results': results,
                     'submitbutton': submitbutton, 'status':status, 'merged':merged}

            return render(request, 'dashboard/output/search_container.html', context)
        else:
            return render(request, 'dashboard/output/search_container.html')
    else:
        return render(request, 'dashboard/output/search_container.html')





@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def search_multiple_containers(request):
    if request.method == 'GET':
        query = 0
        query= request.GET.get('q')
        print(query)
        merged = []
        
        container_in_gate_queryset = []
        container_out_gate_queryset = []
        if query is not None:
            print('Variable is not None')
            query_list = query.split(',')
            print(query.split(','))
            for query in query_list:
                if query is not None:
                    container_in_gate= Container_in_gate.objects.filter(container_number__iexact=query)
                    container_out_gate = Container_gate_out.objects.filter(container_number__iexact=query)

                    container_in_gate_queryset.append(container_in_gate)
                    container_out_gate_queryset.append(container_out_gate)

            merged1 = chain(container_in_gate_queryset)
            print("this is the for loop")
            for data in merged1:
                if len(data)>1:
                    for data in data:
                        merged.append(data)
                else:
                    for data in data:
                        merged.append(data)
        else:
            print('Variable is None')
        submitbutton= request.GET.get('submit')
        
        context={'submitbutton': submitbutton, 'merged':merged}

        return render(request, 'dashboard/output/search_multiple_containers.html', context)
           
    else:
        return render(request, 'dashboard/output/search_multiple_containers.html')





@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def chassis_loc(request):
    loc = Container_in_gate.objects.values('yard_location')
    loc_list = []
    queryset = []
    for yard_loc in loc.values():
        if len(yard_loc['yard_location'])>2:
            loc = yard_loc['yard_location']
            loc_list.append(loc)

    un_loc = list(set(loc_list))
    for un_loc in un_loc:
        query = list(Container_in_gate.objects.filter(yard_location__icontains=un_loc))

        print(query)
        
        if len(query) >1: 
            for query in query:
                if query not in queryset:
                    queryset.append(query)
        else:
            for query in query:
                if query not in queryset:
                    queryset.append(query)
    
    container_type= ContainerType.objects.all()
    search_count = len(queryset)
    shipping_name= Steamship.objects.all()
    context={'results': queryset,
    'search_count': search_count,
     'container_type':list(container_type),
     'shipping_name':list(shipping_name),
                    }
    return render(request, 'dashboard/output/container_in_gate.html', context)



@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def locations_01(request):
    locations = Container_in_gate.objects.values('yard_location').annotate(number_of_entries=Count('yard_location'))
    containers_l = Container_in_gate.objects.all()
    return render(request, 'dashboard/output/locations.html', {'locations': list(locations), 'contianers':list(containers_l)})



@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def search_container_in_gate(request):
    if request.method == 'GET':
        qs = Container_in_gate.objects.all()
        container_number= request.GET.get('container_number')
        yard_location= request.GET.get('yard_location')
        container_status= request.GET.get('container_status')
        steamshiping_line= request.GET.get('steamshiping_line')
        containerType= request.GET.get('containerType')
        efrom= request.GET.get('efrom')
        eto= request.GET.get('eto')
        dfrom= request.GET.get('dfrom')
        dto= request.GET.get('dto')
        notes= request.GET.get('notes')
        
        submitbutton= request.GET.get('submit')
        
        if container_number != '':
            qs = qs.filter(container_number__iexact=container_number)

        if yard_location != '':
            qs = qs.filter(yard_location__icontains=yard_location)

        if container_status != '':
            qs = qs.filter(container_status__icontains=container_status)

        if steamshiping_line != '':
            qs = qs.filter(steamshiping_line__shipping_name__icontains=steamshiping_line)

        if containerType != '':
            qs = qs.filter(containerType__in=containerType)

        if efrom != '' and  eto != '' :
            qs = qs.filter(created_on__gte=efrom, created_on__lte = eto)

        if dfrom != '' and  dto != '' :
            qs = qs.filter(delivery_date__gte=dfrom, delivery_date__lte = dto)
        
        if notes != '':
            qs = qs.filter(comments__icontains=notes)

        query_set = Container_in_gate.objects.order_by('-created_on')
        global search_container_in_gate
        search_container_in_gate = qs

        count = qs.count()
        container_type= ContainerType.objects.all()
        shipping_name= Steamship.objects.all()
        context={'results': list(qs),
                    'container_type':list(container_type),
                    'shipping_name':list(shipping_name),
                    'search_count':count,
                     'submitbutton': submitbutton}
        return render(request, 'dashboard/output/container_in_gate.html', context)
        
    else:
        return render(request, 'dashboard/output/container_in_gate.html')




@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def search_container_out_gate(request):
    if request.method == 'GET':
        qs = Container_gate_out.objects.all()
        container_number= request.GET.get('container_number')
        yard_location= request.GET.get('yard_location')
        container_status= request.GET.get('container_status')
        steamshiping_line= request.GET.get('steamshiping_line')
        efrom= request.GET.get('efrom')
        eto= request.GET.get('eto')
        dfrom= request.GET.get('dfrom')
        dto= request.GET.get('dto')
        ofrom= request.GET.get('ofrom')
        oto= request.GET.get('oto')
        submitbutton= request.GET.get('submit')
        container_type= ContainerType.objects.all()
        shipping_name= Steamship.objects.all()
        if container_number != '':
            qs = qs.filter(container_number__iexact=container_number)

        if yard_location != '':
            qs = qs.filter(yard_location__icontains=yard_location)

        if container_status != '':
            qs = qs.filter(container_status__icontains=container_status)

        if steamshiping_line != '':
            qs = qs.filter(steamshiping_line__icontains=steamshiping_line)

        if efrom != '' and  eto != '' :
            qs = qs.filter(created_on__gte=efrom, created_on__lte = eto)

        if dfrom != '' and  dto != '' :
            qs = qs.filter(delivery_date__gte=dfrom, delivery_date__lte = dto)

        elif ofrom != '' and  oto != '' :
            qs = qs.filter(created_on__gte=ofrom, created_on__lt = oto)

        qs = qs.order_by('-created_on')
        search_count = qs.count()
        query_set = Container_gate_out.objects.order_by('-created_on')
        count = query_set.count()
        context={'results': list(qs),
                    'container_type':list(container_type),
                    'shipping_name':list(shipping_name),
                     'submitbutton': submitbutton,
                     'search_count': search_count,
                     'count': count, 
                     'container_out_gate': list(query_set)}
        return render(request, 'dashboard/output/container_out_gate.html', context)
        
    else:
        return render(request, 'dashboard/output/container_out_gate.html')









#****************************************************************************
#Container out gate


@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def gate_out(request, pk):
    data = Container_in_gate.objects.all().get(id=pk)
    # b = Gatecheck(
    #     type = 'IN',
    #     created_on = data.created_on,
    #     trucking_company = data.trucking_company,
    #     outer_company = data.outer_company,
    #     truck_number = data.truck_number,
    #     manual_truck_number = data.manual_truck_number,
    #     chassis_number = data.chassis_number,
    #     comments = data.comments,
    #     user = data.user
    # )
    # b.save()
    print(data.container_status)
    if data.container_status == 'storage':
        query_set = Container_in_gate.objects.order_by('-created_on')[:50]
        today = datetime.date.today()
        container_type= ContainerType.objects.all()
        shipping_name= Steamship.objects.all()
        count = Container_in_gate.objects.count()
        err = "This container cannot be outgated as it is in storage state"
        return render(request, 'dashboard/output/container_in_gate.html', {'err':err,'container_ingate': list(query_set), 'in_count': count,'shipping_name':list(shipping_name), 'container_type':list(container_type)})
    elif request.method == 'POST':
        gate_out = Add_Container_Gate_Out(request.POST)
        if gate_out.is_valid():
            gate_out = gate_out.save(commit=False)

            gate_out.user= request.user
            gate_out.container_number = data.container_number
            gate_out.enter_date = data.created_on
            gate_out.containerType = data.containerType
            gate_out.container_plug_check = data.container_plug_check
            gate_out.yard_location = data.yard_location
            gate_out.container_status = data.container_status
            gate_out.booking_number = data.booking_number
            gate_out.in_gate_user = data.user
            gate_out.seal_number = data.seal_number
            gate_out.delivery_date = data.delivery_date
            gate_out.destination = data.destination
            gate_out.steamshiping_line = data.steamshiping_line
            gate_out.weight = data.weight
            gate_out.weight_type = data.weight_type
            gate_out.trucking_company_in = data.trucking_company
            gate_out.outer_company_in = data.outer_company
            gate_out.outer_company_manual_in = data.outer_company_manual
            gate_out.truck_number_in = data.truck_number
            gate_out.manual_truck_number_in = data.manual_truck_number
            gate_out.chassis_number_in = data.chassis_number
            gate_out.comments_in = data.comments

            date_format = "%Y-%m-%d"
            present_date = datetime.datetime.strptime(str(datetime.datetime.now().date()), date_format)
            created_on = datetime.datetime.strptime(str(data.created_on.date()), date_format)
            gate_out.total_days = (present_date - created_on).days + 1
            days = gate_out.total_days
            gate_out.invoice  = 35+20*(days-1)
            
            gate_out = gate_out.save()


            Container_in_gate.objects.filter(id=pk).delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        gate_out = Add_Container_Gate_Out()

    return render(request, 'dashboard/input/add_direct_out_gate.html', {'gate_out': gate_out,'data':data})
    

@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def detail_container_out_gate(request, pk):
    data = Container_gate_out.objects.get(id=pk)
    return render(request, 'dashboard/detail/container_out_gate.html', {'data': data})



@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def container_out_gate(request):
    query_set = Container_gate_out.objects.order_by('-created_on')[:50]
    return render(request, 'dashboard/output/container_out_gate.html', {'container_out_gate': list(query_set)})



@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def update_container_out_gate(request, pk):
    data = Container_gate_out.objects.get(id=pk)
    update_container_out_gate = Update_Container_Out_Gate(instance = data)
    if request.method == 'POST':
        update_container_out_gate = Update_Container_Out_Gate(request.POST, instance=data)
        if update_container_out_gate.is_valid():
            update_container_out_gate = data.save()
            return HttpResponseRedirect('/dashboard/container_out_gate/')
    return render(request, 'dashboard/input/update_container_out_gate.html', {'data': update_container_out_gate})


@login_required
@allowed_user(allowed_roles=['admin'])
def delete_container_out_gate(request, pk):
    data = Container_gate_out.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/dashboard/container_out_gate/')
    return render(request, 'dashboard/delete/container_out_gate.html', {'data': data})





#********************************************************************
# multiple locations



def multiple_locations(request):
    if request.method == 'GET':
        query= request.GET.getlist('change_loc')
        submitbutton= request.GET.get('submit')
        updated_loc = request.GET.get('updated_loc')
        for item in query:
            container = Container_in_gate.objects.get(container_number__iexact=item)
            container.yard_location = updated_loc
            container.save(update_fields=['yard_location'])
        container_ingate = Container_in_gate.objects.order_by('-created_on')
        context={'container_ingate': container_ingate}
        return render(request, 'dashboard/output/container_in_gate.html', context)
    else:
        return render(request, 'dashboard/output/container_in_gate.html')



def multiple_search_locations(request):
    if request.method == 'GET':
        query= request.GET.getlist('change_search_loc')
        submitbutton= request.GET.get('submit')
        updated_search_loc = request.GET.get('updated_search_loc')
        for item in query:
            container = Container_in_gate.objects.get(container_number__iexact=item)
            container.yard_location = updated_search_loc
            container.save(update_fields=['yard_location'])
        container_ingate = Container_in_gate.objects.order_by('-created_on')
        context={'container_ingate': container_ingate}
        return render(request, 'dashboard/output/container_in_gate.html', context)
    else:
        return render(request, 'dashboard/output/container_in_gate.html')




#***********************************************************************
# Prepull 


@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def prepull(request):
    query_set = Prepull.objects.order_by('container_number')
    count = query_set.count()
    return render(request, 'dashboard/output/prepull.html', {'prepull': list(query_set), 'count': count})


@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def update_view_prepull(request,pk):
    query_set = Prepull.objects.order_by('-created_on')
    
    data = Prepull.objects.get(id=pk)
    add_prepull = Add_Prepull(instance = data)

    if request.method == 'POST':
        add_prepull = Add_Prepull(request.POST, instance=data)
        if add_prepull.is_valid():
            add_prepull = add_prepull.save()
            return HttpResponseRedirect('/dashboard/prepull/')

    return render(request, 'dashboard/output/test.html', {'add_prepull': add_prepull, 'prepull':list(query_set)})



@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def add_prepull(request):
    err=" "
    if request.method == 'POST':
        add_prepull = Add_Prepull(request.POST)
        if add_prepull.is_valid():
            add_prepull = add_prepull.save(commit=False)
            add_prepull.user= request.user

            if Prepull.objects.filter(container_number=add_prepull.container_number).exists():
                err= "container already prepulled"
                add_prepull = Add_Prepull()
                return render(request, 'dashboard/input/add_prepull.html', {'add_prepull': add_prepull,'err':err})
            else:
                add_prepull = add_prepull.save()
                return HttpResponseRedirect('/dashboard/add_prepull')
                
    else:
        add_prepull = Add_Prepull()

    return render(request, 'dashboard/input/add_prepull.html', {'add_prepull': add_prepull,'err':err})


@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def update_prepull(request, pk):
    data = Prepull.objects.get(id=pk)
    add_prepull = Add_Prepull(instance = data)

    if request.method == 'POST':
        add_prepull = Add_Prepull(request.POST, instance=data)
        if add_prepull.is_valid():
            add_prepull = add_prepull.save()
            return HttpResponseRedirect('/dashboard/prepull/')

    return render(request, 'dashboard/input/add_prepull.html', {'add_prepull': add_prepull})


@login_required
@allowed_user(allowed_roles=['admin'])
def delete_prepull(request, pk):
    data = Prepull.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/dashboard/prepull/')

    return render(request, 'dashboard/delete/prepull.html', {'data': data})




def ml_inbound_dt(request):
    if request.method == 'GET':
        query= request.GET.getlist('inbound_date')
        submitbutton= request.GET.get('submit')
        inbdt_gt = request.GET.get('inbdt_gt')
        inbdt_lt = request.GET.get('inbdt_lt')
        for item in query:
            container = Prepull.objects.get(container_number__iexact=item)
            container.inbound_date_lt = inbdt_lt
            container.inbound_date_gt = inbdt_gt
            container.save(update_fields=['inbound_date_gt','inbound_date_lt'])
        prepull = Prepull.objects.order_by('-created_on')
        context={'prepull': prepull}
        return render(request, 'dashboard/output/prepull.html', context)
    else:
        return render(request, 'dashboard/output/prepull.html')





@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def search_prepull(request):
    if request.method == 'GET':
        qs = Prepull.objects.all()
        container_number= request.GET.get('container_number')
        submitbutton= request.GET.get('submit')
        search_count = qs.count()
        if container_number != '':
            qs = qs.filter(container_number__icontains=container_number)
        
        query_set = Prepull.objects.order_by('-created_on')
        
        context={'results': list(qs),
                'search_count':search_count,
                     'submitbutton': submitbutton, 'prepull': list(query_set)}
        return render(request, 'dashboard/output/prepull.html', context)
        
    else:
        return render(request, 'dashboard/output/prepull.html')



@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def in_gate(request, pk):
    data = Prepull.objects.all().get(id=pk)
    if request.method == 'POST':
        in_gate = Add_In_Gate(request.POST)
        if in_gate.is_valid():
            in_gate = in_gate.save(commit=False)

            b = Gatecheck(
                type = 'IN',
                created_on = data.created_on,
                container_number = data.container_number,
                trucking_company = in_gate.trucking_company,
                outer_company = in_gate.outer_company,
                truck_number = in_gate.truck_number,
                manual_truck_number = in_gate.manual_truck_number,
                chassis_number = in_gate.chassis_number,
                comments = in_gate.comments,
                user = request.user
            )
            b.save()

            in_gate.user= request.user
            in_gate.container_number = data.container_number
            in_gate.created_on = data.created_on
            in_gate.steamshiping_line = data.steamshiping_line
            in_gate.delivery_date = data.delivery_date
            in_gate.destination = data.destination
            in_gate.weight = data.weight
            in_gate.weight_type = data.weight_type
            in_gate.prepull_notes = data.comments
            in_gate = in_gate.save()
            Prepull.objects.filter(id=pk).delete()
            return HttpResponseRedirect('/dashboard/container_in_gate/')
    else:
        in_gate = Add_In_Gate()

    return render(request, 'dashboard/input/add_in_gate.html', {'in_gate': in_gate})
    

# ******************************************************************************************
# Upcoming deliveries

@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def upcoming_deliveries(request):
    query_set = Container_in_gate.objects.all()
    today = query_set.filter(delivery_date__date=date.today())
    tom = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow = query_set.filter(delivery_date__date=tom)
    today_count = today.count()
    tom_count = tomorrow.count()
    return render(request, 'dashboard/more/upcoming_deliveries.html', {'container_ingate': list(query_set), 'today': list(today), 'tomorrow':list(tomorrow), 'today_count':today_count, 'tom_count':tom_count})



@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def search_deliveries(request):
    if request.method == 'GET':
        qs = Container_in_gate.objects.all()
        container_number= request.GET.get('container_number')
        submitbutton= request.GET.get('submit')
        today = qs.filter(delivery_date__date=date.today())
        tom = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow = qs.filter(delivery_date__date=tom)
        if container_number != '':
            qs = qs.filter(container_number__icontains=container_number)
        context={
                    'results': list(qs),
                    'submitbutton': submitbutton, 
                    'today': list(today), 
                    'tomorrow':list(tomorrow)
                }
        return render(request, 'dashboard/more/upcoming_deliveries.html', context)
    else:
        return render(request, 'dashboard/more/upcoming_deliveries.html')






# ******************************************************************************************
# chassis damage



def add_chassis_damage(request):
  
    if request.method == 'POST':
        form = Add_Chassis_Damage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/chassis_damage/')
    else:
        form = Add_Chassis_Damage()
    return render(request, 'dashboard/more/chassis_damage.html', {'form' : form})



@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def chassis_damage(request):
    query_set = Chassis_Damage.objects.all()
    count = query_set.count()
    return render(request, 'dashboard/output/chassis_damage.html', {'data': list(query_set), 'count': count})



@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def update_chassis_damage(request, pk):
    data = Chassis_Damage.objects.get(id=pk)
    form = Add_Chassis_Damage(instance = data)

    if request.method == 'POST':
        form = Add_Chassis_Damage(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect('/dashboard/chassis_damage/')

    return render(request, 'dashboard/more/chassis_damage.html', {'form': form})


@login_required
@allowed_user(allowed_roles=['admin'])
def delete_chassis_damage(request, pk):
    data = Chassis_Damage.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/dashboard/chassis_damage/')
    return render(request, 'dashboard/more/chassis_damage.html')





# ******************************************************************************************
# chassis corrected


@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def chassis_corr(request, pk):
    data = Chassis_Damage.objects.all().get(id=pk)
    if request.method == 'POST':
        corr = Add_Chassis_Corr(request.POST)
        if corr.is_valid():
            corr = corr.save(commit=False)
            corr.chassis_number = data.chassis_number
            corr.unit_number = data.unit_number
            corr.chassis_problem = data.chassis_problem
            corr.location = data.location
            corr.tag_number = data.tag_number
            corr.assignment = data.assignment
            corr.dmg_img = data.dmg_img
            corr = corr.save()
            Chassis_Damage.objects.filter(id=pk).delete()
            return HttpResponseRedirect('/dashboard/chassis_corr/')
    else:
        corr = Add_Chassis_Corr()

    return render(request, 'dashboard/input/chassis_corr.html', {'corr': corr})



@login_required
def all_chassis_corr(request):
    query_set = Chassis_Corr.objects.all()
    count = query_set.count()
    return render(request, 'dashboard/output/chassis_corr.html', {'data': list(query_set), 'count': count})


@login_required
@allowed_user(allowed_roles=['admin','dispatch','gate','crane'])
def update_chassis_corr(request, pk):
    data = Chassis_Corr.objects.get(id=pk)
    form = Add_Chassis_Corr(instance = data)
    if request.method == 'POST':
        form = Add_Chassis_Corr(request.POST, instance=data)
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect('/dashboard/chassis_damage/')
    return render(request, 'dashboard/input/chassis_corr.html', {'corr': form})


@login_required
@allowed_user(allowed_roles=['admin'])
def delete_chassis_corr(request, pk):
    data = Chassis_Corr.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/dashboard/chassis_damage/')
    return render(request, 'dashboard/more/chassis_damage.html')

