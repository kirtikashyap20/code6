from re import A
from django import forms
from .models import Gatecheck, Yard_location, ContainerType, Chassis_number, Steamship, Container_in_gate, Container_gate_out, Truck, TruckingCompany, Driver, Prepull, Chassis_Damage, Chassis_Corr


class Add_Chassis_Corr(forms.ModelForm):
    class Meta:
        model = Chassis_Corr
        fields = ['repaired_by']
        widgets = {
            'repaired_by' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
        }




class Add_Chassis_Damage(forms.ModelForm):
    class Meta:
        model = Chassis_Damage
        fields = ['chassis_number','unit_number','chassis_problem','location','tag_number','assignment','eta','dmg_img']
        widgets = {
            'chassis_number' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'unit_number' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
                
            ),
            'chassis_problem' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'location' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'tag_number' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'assignment' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'eta' : forms.DateTimeInput(
                attrs={
                    'id':'basicFlatpickr',
                    'class':'form-control mb-4 flatpickr flatpickr-input active',
                    'readonly':'readonly',
                    'placeholder':''
                }
            ),
            'dmg_img' : forms.FileInput(
                attrs={
                    'class':'form-control mb-4',
                    'multiple':True
                }
            )
        }


class Add_Yard_Location(forms.ModelForm):
    class Meta:
        model = Yard_location
        fields = ['location']
        widgets = {
            'location' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            )
        }


class Add_yl(forms.ModelForm):
    class Meta:
        model = Container_in_gate
        fields = ['container_number', 'yard_location']
        widgets = {
            'container_number' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':'', 
                    'readonly': True
                }
            ),
            'yard_location' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            )
        }



class Add_Container_Type(forms.ModelForm):
    class Meta:
        model = ContainerType
        fields = ['containerTypeAndSize']
        widgets = {
            'containerTypeAndSize' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            )
        }

class Add_Container_Gate_Out(forms.ModelForm):
    class Meta:
        model = Container_gate_out
        fields = ['container_number','trucking_company', 'outer_company','outer_company_manual','truck_number', 'manual_truck_number', 'chassis_number','comments']
        widgets = {
            'container_number' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'readonly':True
                }
            ),
            'trucking_company' : forms.Select(
                attrs={
                    'class':'form-control  mb-4 trucking_company',
                    'placeholder':''
                }
            ),
            'outer_company' : forms.Select(
                attrs={
                    'class':'form-control  mb-4 outer_company',
                    'placeholder':''
                }
            ),
            'outer_company_manual' : forms.TextInput(
                attrs={
                    'class':'form-control  mb-4 outer_company_manual',
                    'placeholder':''
                }
            ),
            'truck_number' : forms.Select(
                attrs={
                    'class':'form-control  mb-4 truck_number',
                    'placeholder':''
                }
            ),
            'manual_truck_number' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char mb-4 manual_truck_number',   
                    'placeholder':''
                }
            ),
            'chassis_number' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'comments' : forms.TextInput(
                attrs={
                    'class':'form-control  mb-4',
                    'placeholder':''
                }
            ),
        }







class Add_Driver(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['driver_name', 'license_number']
        widgets = {
            'driver_name' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'license_number' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            )
        }



class Add_Steamship(forms.ModelForm):
    class Meta:
        model = Steamship
        fields = ['shipping_name']
        widgets = {
            'shipping_name' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            )
        }




class Add_Truck(forms.ModelForm):
    class Meta:
        model = Truck
        fields = ['unit_number','driver','vin','plate_number','year','make']
        widgets = {
            'unit_number' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'driver' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'vin' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'plate_number' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'year' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'make' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            )
        }


class Add_Trucking_Company(forms.ModelForm):
    class Meta:
        model = TruckingCompany
        fields = ['company_name','company_phone','company_phone','company_email','company_address']
        widgets = {
            'company_name' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'company_phone' : forms.NumberInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'company_email' : forms.EmailInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'company_address' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
        }



class Add_Container_In_Gate(forms.ModelForm):
    class Meta:
        model = Container_in_gate
        fields = ['container_number','containerType','container_plug_check','yard_location','container_status','booking_number','seal_number','delivery_date','destination','weight','weight_type','steamshiping_line','trucking_company','outer_company','outer_company_manual','truck_number','manual_truck_number','chassis_number','comments']
        widgets = {
            'container_number' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':'',
                    'pattern':'[A-Za-z]{4}[0-9]{7}'
                }
            ),
            'containerType' : forms.Select(
                attrs={
                    'class':'form-control mb-4 in-container-type',
                    'placeholder':''
                }
            ),
            'container_plug_check' : forms.Select(
                attrs={
                    'id':'plug',
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'yard_location' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'delivery_date' : forms.DateTimeInput(
                attrs={
                    'id':'basicFlatpickr',
                    'class':'form-control mb-4 flatpickr flatpickr-input active',
                    'readonly':'readonly',
                    'placeholder':''

                }
            ),
            'container_status' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':'NA'
                }
            ),
            'booking_number' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4 booking_number',
                    'placeholder':''
                }
            ),
            'seal_number' : forms.TextInput(


                attrs={
                    'class':'form-control no_special_char mb-4 seal_number',
                    'placeholder':''
                }
            ),
            'weight' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char mb-4 weight',
                    'placeholder':''
                }
            ),
            'weight_type' : forms.Select(
                attrs={
                    'class':'form-control mb-4 weight',
                    'placeholder':''
                }
            ),
            'destination' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'steamshiping_line' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'trucking_company' : forms.Select(
                attrs={
                    'class':'form-control mb-4 in-trucking_company',
                    'placeholder':''
                }
            ),
            'outer_company' : forms.Select(
                attrs={
                    'class':'form-control mb-4 in-external-company',
                    'placeholder':''
                }
            ),
            'outer_company_manual' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4 in-container_company_manual',
                    'placeholder':''
                }
            ),
            'truck_number' : forms.Select(
                attrs={
                    'class':'form-control mb-4 in-truck_number',
                    'placeholder':''
                }
            ),
            'manual_truck_number' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char mb-4 in-manual_truck_number',
                    'placeholder':''
                }
            ),
            'chassis_number' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'comments' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
        }

class Add_Gatecheck(forms.ModelForm):
    class Meta:
        model = Gatecheck
        fields = ['type', 'trucking_company','outer_company','outer_company_manual', 'truck_number', 'manual_truck_number','chassis_number','comments']
        widgets = {
            'type' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),

            'trucking_company' : forms.Select(
                attrs={
                    'class':'form-control mb-4 trucking_company_gate',
                    'placeholder':'Select Company'
                }
            ),
            'outer_company' : forms.Select(
                attrs={
                    'class':'form-control mb-4 outer_company_gate',
                    'placeholder':'Select Company'
                }
            ),
            'outer_company_manual' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4 outer_company_manual_gate',
                    'placeholder':''
                }
            ),
            'truck_number' : forms.Select(
                attrs={
                    'class':'form-control mb-4 truck_number_gate',
                    'placeholder':''
                }
            ),
            
            'manual_truck_number' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4 manual_truck_number_gate',
                    'placeholder':''
                }
            ),
            'chassis_number' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'comments' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            )
        }




class Update_Container_Out_Gate(forms.ModelForm):
    class Meta:
        model = Container_gate_out
        fields = ['container_number','containerType','container_plug_check','yard_location','container_status','booking_number','seal_number','delivery_date','destination','weight','weight_type','steamshiping_line','trucking_company_in','outer_company_in','outer_company_manual_in','truck_number_in','manual_truck_number_in','chassis_number_in', 'trucking_company', 'outer_company','outer_company_manual','truck_number','manual_truck_number', 'chassis_number','comments']
        widgets = {
            'container_number' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':'',
                    'pattern':'[A-Za-z]{4}[0-9]{7}'
                }
            ),
            'containerType' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'container_plug_check' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'yard_location' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'delivery_date' : forms.DateTimeInput(
                attrs={
                    'id':'dateTimeFlatpickr',
                    'class':'form-control mb-4 flatpickr flatpickr-input active',
                    'readonly':'readonly',
                    'placeholder':''

                }
            ),
            'container_status' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':'NA'
                }
            ),
            'booking_number' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'seal_number' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'weight' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'weight_type' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'destination' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'steamshiping_line' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'trucking_company_in' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'outer_company_in' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'outer_company_manual_in' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'truck_number_in' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'manual_truck_number_in' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'chassis_number_in' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'special_notes_in' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'trucking_company' : forms.Select(
                attrs={
                    'class':'form-control  mb-4 ',
                    'placeholder':''
                }
            ),
            'outer_company' : forms.Select(
                attrs={
                    'class':'form-control  mb-4 ',
                    'placeholder':''
                }
            ),
            'outer_company_manual' : forms.TextInput(
                attrs={
                    'class':'form-control  mb-4 ',
                    'placeholder':''
                }
            ),
            'truck_number' : forms.Select(
                attrs={
                    'class':'form-control  mb-4 ',
                    'placeholder':''
                }
            ),
            'manual_truck_number' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char  mb-4 ',   
                    'placeholder':''
                }
            ),
            'chassis_number' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'comments' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
        }

 


class Search_Container_In_Gate(forms.ModelForm):
    class Meta:
        model = Container_in_gate
        fields = ['container_number','containerType','container_plug_check','yard_location','container_status','booking_number','seal_number','delivery_date','destination','weight','weight_type','steamshiping_line','trucking_company','outer_company','outer_company_manual','truck_number','manual_truck_number','chassis_number','comments']
        widgets = {
            'container_number' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':'',
                    'pattern':'[A-Za-z]{4}[0-9]{7}'
                }
            ),
            'containerType' : forms.Select(
                attrs={
                    'class':'form-control mb-4 in-container-type',
                    'placeholder':''
                }
            ),
            'container_plug_check' : forms.Select(
                attrs={
                    'id':'plug',
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'yard_location' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'delivery_date' : forms.DateTimeInput(
                attrs={
                    'id':'dateTimeFlatpickr',
                    'class':'form-control mb-4 flatpickr flatpickr-input active',
                    'readonly':'readonly',
                    'placeholder':''

                }
            ),
            'container_status' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':'NA'
                }
            ),
            'booking_number' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4 booking_number',
                    'placeholder':''
                }
            ),
            'seal_number' : forms.TextInput(


                attrs={
                    'class':'form-control mb-4 seal_number',
                    'placeholder':''
                }
            ),
            'weight' : forms.NumberInput(
                attrs={
                    'class':'form-control mb-4 weight',
                    'placeholder':''
                }
            ),
            'weight_type' : forms.Select(
                attrs={
                    'class':'form-control mb-4 weight',
                    'placeholder':''
                }
            ),
            'destination' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'steamshiping_line' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'trucking_company' : forms.Select(
                attrs={
                    'class':'form-control mb-4 in-trucking_company',
                    'placeholder':''
                }
            ),
            'outer_company' : forms.Select(
                attrs={
                    'class':'form-control mb-4 in-external-company',
                    'placeholder':''
                }
            ),
            'outer_company_manual' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4 in-container_company_manual',
                    'placeholder':''
                }
            ),
            'truck_number' : forms.Select(
                attrs={
                    'class':'form-control mb-4 in-truck_number',
                    'placeholder':''
                }
            ),
            'manual_truck_number' : forms.NumberInput(
                attrs={
                    'class':'form-control mb-4 in-manual_truck_number',
                    'placeholder':''
                }
            ),
            'chassis_number' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'comments' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
        }



class Add_Prepull(forms.ModelForm):
    class Meta:
        model = Prepull
        fields = ['container_number','steamshiping_line','delivery_date','destination','weight','weight_type','comments']
        widgets = {
            'container_number' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':'',
                    'pattern':'[A-Za-z]{4}[0-9]{7}'
                }
            ),
            'steamshiping_line' : forms.Select(
                attrs={
                    'class':'form-control mb-4 in-container-type',
                    'placeholder':''
                }
            ),
            'delivery_date' : forms.DateTimeInput(
                attrs={
                    'id':'basicFlatpickr',
                    'class':'form-control mb-4 flatpickr flatpickr-input active',
                    'readonly':'readonly',
                    'placeholder':''

                }
            ),
            'weight' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char mb-4 weight',
                    'placeholder':''
                }
            ),
            'weight_type' : forms.Select(
                attrs={
                    'class':'form-control mb-4 weight',
                    'placeholder':''
                }
            ),
            'destination' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'comments' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
        }


class Add_Prepull_test(forms.ModelForm):
    class Meta:
        model = Prepull
        fields = ['container_number','steamshiping_line','delivery_date','destination','weight','weight_type','comments']
        widgets = {
            'container_number' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':'',
                    'pattern':'[A-Za-z]{4}[0-9]{7}'
                }
            ),
            'steamshiping_line' : forms.Select(
                attrs={
                    'class':'form-control mb-4 in-container-type',
                    'placeholder':''
                }
            ),
            'delivery_date' : forms.DateTimeInput(
                attrs={
                    'id':'basicFlatpickr',
                    'class':'form-control mb-4 flatpickr flatpickr-input active',
                    'readonly':'readonly',
                    'placeholder':''

                }
            ),
            'weight' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'weight_type' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'destination' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'comments' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
        }


class Add_In_Gate(forms.ModelForm):
    class Meta:
        model = Container_in_gate
        fields = ['container_plug_check','yard_location','containerType','container_status','booking_number','seal_number','trucking_company','outer_company','outer_company_manual','truck_number','manual_truck_number','chassis_number']
        widgets = {
            'container_plug_check' : forms.Select(
                attrs={
                    'id':'plug',
                    'class':'form-control mb-4',
                    'placeholder':''
                }
            ),
            'yard_location' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
            'containerType' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':'NA'
                }
            ),
            'container_status' : forms.Select(
                attrs={
                    'class':'form-control mb-4',
                    'placeholder':'NA'
                }
            ),
            'booking_number' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4 booking_number',
                    'placeholder':''
                }
            ),
            'seal_number' : forms.TextInput(


                attrs={
                    'class':'form-control no_special_char mb-4 seal_number',
                    'placeholder':''
                }
            ),
            'trucking_company' : forms.Select(
                attrs={
                    'class':'form-control mb-4 in-trucking_company',
                    'placeholder':''
                }
            ),
            'outer_company' : forms.Select(
                attrs={
                    'class':'form-control mb-4 in-external-company',
                    'placeholder':''
                }
            ),
            'outer_company_manual' : forms.TextInput(
                attrs={
                    'class':'form-control mb-4 in-container_company_manual',
                    'placeholder':''
                }
            ),
            'truck_number' : forms.Select(
                attrs={
                    'class':'form-control mb-4 in-truck_number',
                    'placeholder':''
                }
            ),
            'manual_truck_number' : forms.NumberInput(
                attrs={
                    'class':'form-control no_special_char mb-4 in-manual_truck_number',
                    'placeholder':''
                }
            ),
            'chassis_number' : forms.TextInput(
                attrs={
                    'class':'form-control no_special_char mb-4',
                    'placeholder':''
                }
            ),
        }