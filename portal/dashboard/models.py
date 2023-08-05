from django.db import models
from django.db.models.deletion import PROTECT, CASCADE, RESTRICT, SET_NULL

from authentication.models import User
#from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


# Create your models here.

class Yard_location(models.Model):
    location = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    def __str__(self) -> str:
        return self.location

    class Meta:
        ordering = ['location']


class TruckingCompany(models.Model):
    
    company_name = models.CharField(max_length=255)
    company_phone = models.IntegerField(null=True, blank=True)
    company_email = models.EmailField(null=True, blank=True)
    company_address = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    def __str__(self) -> str:
        return self.company_name

    class Meta:
        ordering = ['company_name']


class Driver(models.Model):
    
    driver_name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255,blank=True, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    def __str__(self) -> str:
        return self.driver_name

    class Meta:
        ordering = ['driver_name']


class Truck(models.Model):
    
    unit_number = models.IntegerField()
    driver = models.ForeignKey(Driver, on_delete=SET_NULL,blank=True, null = True)
    vin = models.CharField(max_length=130,blank=True, null = True)
    plate_number = models.IntegerField(blank=True, null = True)
    year = models.IntegerField(null=True, blank=True)
    make = models.CharField(max_length=70, null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    def __str__(self) -> str:
        return str(self.unit_number)

    class Meta:
        ordering = ['unit_number']


class ContainerType(models.Model):
    containerTypeAndSize = models.CharField(max_length=255, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    def __str__(self) -> str:
        return self.containerTypeAndSize

    class Meta:
        ordering = ['containerTypeAndSize']



class Steamship(models.Model):
    shipping_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    def __str__(self) -> str:
        return self.shipping_name

    class Meta:
        ordering = ['shipping_name']


class Chassis_number(models.Model):
    chassis_number = models.IntegerField()
    def __str__(self) -> str:
        return str(self.chassis_number)

    class Meta:
        ordering = ['chassis_number']


class Container_in_gate(models.Model):
    NA = 'na'
    PLUG_IN = 'in'
    PLUG_OUT = 'out'

    CONTAINER_PLUG_CHECK=[
        (NA,'N/A'),
        (PLUG_IN, 'Plugged In'),
        (PLUG_OUT, 'Plugged Out'),
    ]
    
    LOAD = 'load'
    EMPTY = 'empty'
    DROP = 'drop'
    SWITCH = 'switch'
    TERMINATED = 'terminated'
    STORAGE = 'storage'
    PICK_UP = 'pick up'

    CONTAINER_STATUS = [
        (LOAD,'Load'),
        (EMPTY,'Empty'),
        (DROP, 'DROP'),
        (SWITCH, 'SWITCH'),
        (TERMINATED, 'TERMINATED'),
        (STORAGE, 'STORAGE'),
        (PICK_UP, 'PICK UP')
    ]
    
    
    
    type = "in"
    #user_detail = models.ForeignKey(User, default=User, on_delete= SET_NULL, null = True)
    container_number = models.CharField(max_length=100)
    containerType = models.ForeignKey(ContainerType, on_delete=SET_NULL, null = True)
    container_plug_check = models.CharField(max_length=3, choices= CONTAINER_PLUG_CHECK, default='na', blank=True, null = True)
    yard_location = models.CharField(max_length=100, null = True)
    container_status = models.CharField(max_length=15, choices = CONTAINER_STATUS, blank = False, null =False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    # fields if container is loaded
    booking_number = models.CharField(max_length=100, blank=True, null = True)
    seal_number = models.CharField(max_length=100, blank=True, null = True)
    created_on = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null = True)
    HIGHWAY = 'highway'
    LOCAL = 'local'

    DESTINATION =[
        (HIGHWAY, 'Highway'),
        (LOCAL, 'Local')
    ]

    KG = 'kg'
    LBS = 'lbs'

    WEIGHT_TYPE = [
        (KG,'KILLOGRAMS'),
        (LBS,'LBS')
    ]
    destination = models.CharField(max_length=7, choices=DESTINATION, blank=True, null = True)
    weight = models.PositiveBigIntegerField(null=True, blank=True)
    weight_type = models.CharField(max_length=10, choices = WEIGHT_TYPE,null=True , blank=True)
    
    steamshiping_line = models.ForeignKey(Steamship, on_delete= SET_NULL, blank=True, null = True)

    NULL = '0'
    TRUMP_TRANSPORT = 'trump transport'
    COMPANY =[
        (NULL, 'N/A'),
        (TRUMP_TRANSPORT, 'TRUMP TRANSPORT')
    ]

    trucking_company = models.CharField(max_length=20, choices=COMPANY, null= True, default='trump transport')
    outer_company = models.ForeignKey(TruckingCompany,on_delete = SET_NULL, null = True, blank=True)
    outer_company_manual = models.CharField(max_length=100, blank=True, null = True)
    #container company feilds

    # if the user selects other company 
   
    truck_number = models.ForeignKey(Truck, on_delete = SET_NULL, null = True,blank=True)
    manual_truck_number = models.CharField(max_length=20,null=True, blank=True)

    chassis_number = models.CharField(max_length=20,null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    
    

    def __str__(self) -> str:
        return self.container_number

    class Meta:
        ordering = ['container_number']




class Gatecheck(models.Model):
    IN = 'IN'
    OUT = 'OUT'
    TYPE =[
        (IN, 'IN'),
        (OUT, 'OUT')
    ]
    type = models.CharField(max_length=3, choices=TYPE, null= True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    NULL = '0'
    TRUMP_TRANSPORT = 'trump transport'
    COMPANY =[
        (NULL, 'N/A'),
        (TRUMP_TRANSPORT, 'TRUMP TRANSPORT')
    ]

    trucking_company = models.CharField(max_length=20, choices=COMPANY, null= True, default='trump transport')
    outer_company = models.ForeignKey(TruckingCompany,on_delete = SET_NULL, null = True, blank=True)
    outer_company_manual = models.CharField(max_length=100, blank=True, null = True)

    truck_number = models.ForeignKey(Truck, on_delete = SET_NULL, null = True,blank=True)
    manual_truck_number = models.CharField(max_length=20,null=True, blank=True)
    container_number = models.CharField(max_length=50,null=True, blank=True)
    chassis_number = models.CharField(max_length=20,null=True, blank=True)
    comments = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    # def __str__(self) -> str:
    #     return str(self.unit_number)

    # class Meta:
    #     ordering = ['unit_number']





 
class Container_gate_out(models.Model):
    container_number = models.CharField(max_length=100, blank=True, null = True)
    
    NULL = '0'
    TRUMP_TRANSPORT = 'trump transport'
    COMPANY =[
        (NULL, 'N/A'),
        (TRUMP_TRANSPORT, 'TRUMP TRANSPORT')
    ]
    type = "out"
    trucking_company = models.CharField(max_length=20, choices=COMPANY, null= True, default='trump transport')
    outer_company = models.ForeignKey(TruckingCompany,on_delete = SET_NULL, null = True, blank=True)
    outer_company_manual = models.CharField(max_length=100, blank=True, null = True)

    truck_number = models.ForeignKey(Truck, on_delete = SET_NULL, null = True,blank=True)
    manual_truck_number = models.IntegerField(null=True, blank=True)
    
    chassis_number = models.CharField(max_length=20,null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    in_gate_user =models.CharField(max_length=20,null=True, blank=True)
    #ingate fields
    containerType =models.CharField(max_length=20,null=True, blank=True)
    container_plug_check = models.CharField(max_length=20,null=True, blank=True)
    yard_location = models.CharField(max_length=20,null=True, blank=True)
    container_status = models.CharField(max_length=20,null=True, blank=True)
    # fields if container is loaded
    booking_number = models.CharField(max_length=100, blank=True, null = True)
    seal_number = models.CharField(max_length=100, blank=True, null = True)
    enter_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null = True)
    delivery_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null = True)
    destination = models.CharField(max_length=20,null=True, blank=True)
    weight = models.PositiveBigIntegerField(null=True, blank=True)
    weight_type = models.CharField(max_length=20,null=True, blank=True)
    
    steamshiping_line = models.CharField(max_length=50,null=True, blank=True)
    trucking_company_in = models.CharField(max_length=20,null=True, blank=True)
    outer_company_in = models.CharField(max_length=20,null=True, blank=True)
    outer_company_manual_in = models.CharField(max_length=20,null=True, blank=True)
    #container company feilds

    # if the user selects other company 
    truck_number_in = models.CharField(max_length=20,null=True, blank=True)
    manual_truck_number_in = models.CharField(max_length=20,null=True, blank=True)

    chassis_number_in = models.CharField(max_length=20,null=True, blank=True)
    prepull_notes = models.CharField(max_length=100,null=True, blank=True)
    comments_in = models.CharField(max_length=100,null=True, blank=True)

    total_days = models.CharField(max_length=100,null=True, blank=True)
    invoice = models.CharField(max_length=100,null=True, blank=True)



class Prepull(models.Model):
   
    LOAD = 'load'
    EMPTY = 'empty'

    CONTAINER_STATUS = [
        (LOAD,'Load'),
        (EMPTY,'Empty')
    ]
    type = "prepull"
    container_number = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    steamshiping_line = models.ForeignKey(Steamship, on_delete= SET_NULL, blank=True, null = True)
    created_on = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null = True)
    inbound_date_lt = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null = True)
    inbound_date_gt = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null = True)
    HIGHWAY = 'highway'
    LOCAL = 'local'

    DESTINATION =[
        (HIGHWAY, 'Highway'),
        (LOCAL, 'Local')
    ]

    KG = 'kg'
    LBS = 'lbs'

    WEIGHT_TYPE = [
        (KG,'KILLOGRAMS'),
        (LBS,'LBS')
    ]
    destination = models.CharField(max_length=7, choices=DESTINATION, blank=True, null = True)
    weight = models.PositiveBigIntegerField(null=True, blank=True)
    weight_type = models.CharField(max_length=10, choices = WEIGHT_TYPE,null=True , blank=True)
    comments = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.container_number

    class Meta:
        ordering = ['container_number']





class Chassis_Damage(models.Model):
    chassis_number = models.IntegerField()
    added_on =  models.DateTimeField(auto_now_add=True)
    unit_number = models.ForeignKey(Truck, on_delete = SET_NULL, null = True,blank=True)
    chassis_problem = models.TextField(null=True, blank=True)
    COMING = 'coming soon'
    ROAD = 'on road'
    YARD = 'yard'
    CHASSIS_LOCATION =[
        (COMING, 'coming soon'),
        (ROAD, 'on road'),
        (YARD, 'YARD')
    ]
    location = models.CharField(max_length=20, choices=CHASSIS_LOCATION, null= True)
    tag_number = models.IntegerField(null=True, blank=True)
    assignment = models.CharField(max_length=20, blank=True, null = True)
    dmg_img = models.ImageField(default='/chassis_damages/dmg.jpg', upload_to='chassis_damages', blank=True, null = True)
    eta = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null = True)
    
    def save(self):
        # Opening the uploaded image
        im = Image.open(self.dmg_img) 

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((300, 300))
        im = im.convert('RGB')

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=90)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.dmg_img = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.chassis_number, 'damage/jpeg',
                                        sys.getsizeof(output), None)

        super(Chassis_Damage, self).save()




class Chassis_Corr(models.Model):
    chassis_number = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null = True)
    corr_on =  models.DateTimeField(auto_now_add=True)
    unit_number = models.CharField(max_length=20, blank=True, null= True)
    chassis_problem = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=20, blank=True, null= True)
    tag_number = models.IntegerField(null=True, blank=True)
    assignment = models.CharField(max_length=20, blank=True, null = True)
    dmg_img = models.ImageField(default='chassis_damages/dmg.jpg', upload_to='chassis_corr', blank=True, null = True)
    # corr_img = models.ImageField(default='corr.jpg', upload_to='chassis_corr')
    eta = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null = True)
    repaired_by = models.CharField(max_length=50, blank=True, null = True)