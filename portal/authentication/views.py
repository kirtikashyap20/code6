from datetime import datetime
from itertools import count
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import View
from django.conf import settings

from authentication.models import Punch, Role, Profile
from . import forms
from authentication.forms import AddSetRole, AddPunch, Add_Task
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from dashboard.decorators import allowed_user
from django.contrib.auth import get_user_model
# from django.contrib.gis.utils import GeoIP
from django.utils import timezone
import pytz
import socket
import folium
import ipaddress

from django.views.generic import TemplateView



# Create your views here.


class LoginPageView(View):
    template_name = 'authentication/auth_login.html'
    form_class = forms.LoginForm
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            
            if user is not None:                
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0]
                    print("work")
                    print(ip)
                else:
                    ip = request.META.get('REMOTE_ADDR')
                    print("no")
                    print(ip)
                    if ip != "64.228.147.57":
                        logout(request)
                        return redirect('login')
                    else:
                        print("ip not check")
                return redirect('dashboard/')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    peruser = Punch.objects.filter(user=request.user).order_by("-punch")
    today = timezone.now().date()
    roles = Role.objects.filter(user=request.user, role_punch__date =today)
    last_role = Role.objects.values('role').filter(user=request.user, role_punch__date =today).last()
    return render(request, 'authentication/user_profile.html', { 'peruser':list(peruser), 'today':today, 'roles':list(roles), 'last_role':last_role}) 


#users list
@login_required
@allowed_user(allowed_roles=['admin','billing'])
def users(request):
    User = get_user_model()
    query_set = User.objects.all()
    today = timezone.now().date()
    today_out = Punch.objects.filter(punch__date=today).exclude(status="out")
    online_num = today_out.count()
    print(list(today_out))
    return render(request, 'users/users.html', {'users': list(query_set), 'status':list(today_out), 'count':online_num}) 




@login_required
@allowed_user(allowed_roles=['admin','punch','punch_in'])
def add_punch(request):
    allowed_ip = ["192.168.1.133", "70.31.100.37","68.179.126.165","127.0.0.1"]
    err=" "
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    print(x_forwarded_for)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        print("work")
        print(ip)
        pc = format(ipaddress.IPv4Address('192.168.0.1'))
        
        if ip not in allowed_ip:
            logout(request)
            return redirect('login')
        else:
            today = timezone.now().date()
            data = Punch.objects.filter(punch__date=today).order_by('-punch')
            if request.method == 'POST':
                form = AddPunch(request.POST)
                
                if form.is_valid():   
                    form = form.save(commit=False)
                    print(form.user)
                    get_user = form.user 
                    entered_status = form.status 
                    print ("enters status: ", entered_status)      
                    punch_status = Punch.objects.filter(user=get_user).last()
                    # print(punch_status.status)
                    print("list")
                    if punch_status is not None:
                        if entered_status == "in":
                            print("entered in in loop")
                            if punch_status.status != entered_status:
                                print("entered in in loop")
                                form = form.save()
                                
                            else:
                                if not Punch.objects.filter(status=entered_status, punch__date = today, user=get_user).exists():
                                    form = form.save()
                                else:    
                                    err="punch out first"
                                    print(err)
                                    form = AddPunch()
                                    return render(request, 'users/punch.html', {'form': form,'err':err, 'data':list(data), 'today':today, 'ip':ip}) 
                        else:
                            if punch_status.status != 'out':
                                print("entered in out loop")
                                form = form.save()
                                
                            else: 
                                if not Punch.objects.filter(status=entered_status, punch__date = today, user=get_user).exists():
                                    err="punch in first"
                                    print(err)
                                    form = AddPunch()
                                    return render(request, 'users/punch.html', {'form': form,'err':err, 'data':list(data), 'today':today, 'ip':ip})
                                else:   
                                    err="you are already punched out"
                                    print(err)
                                    form = AddPunch()
                                    return render(request, 'users/punch.html', {'form': form,'err':err, 'data':list(data), 'today':today, 'ip':ip}) 
                    else:
                        if entered_status == 'out':
                            err="punch in first"
                            print(err)
                            form = AddPunch()
                            return render(request, 'users/punch.html', {'form': form,'err':err, 'data':list(data), 'today':today, 'ip':ip})
                        else:
                            form = form.save()

            else:
                form = AddPunch()    
    else:
        ip = request.META.get('REMOTE_ADDR')
        print("no")
        print(ip)
        if ip not in allowed_ip:
            logout(request)
            return redirect('login')
        else:
            today = timezone.now().date()
            data = Punch.objects.filter(punch__date=today).order_by('-punch')
            if request.method == 'POST':
                form = AddPunch(request.POST)
                
                if form.is_valid():   
                    form = form.save(commit=False)
                    print(form.user)
                    get_user = form.user 
                    entered_status = form.status 
                    print ("enters status: ", entered_status)      
                    punch_status = Punch.objects.filter(user=get_user).last()
                    # print(punch_status.status)
                    print("list")
                    if punch_status is not None:
                        if entered_status == "in":
                            print("entered in in loop")
                            if punch_status.status != entered_status:
                                print("entered in in loop")
                                form = form.save()
                                
                            else:
                                if not Punch.objects.filter(status=entered_status, punch__date = today, user=get_user).exists():
                                    form = form.save()
                                else:    
                                    err="punch out first"
                                    print(err)
                                    form = AddPunch()
                                    return render(request, 'users/punch.html', {'form': form,'err':err, 'data':list(data), 'today':today, 'ip':ip}) 
                        else:
                            if punch_status.status != 'out':
                                print("entered in out loop")
                                form = form.save()
                                
                            else: 
                                if not Punch.objects.filter(status=entered_status, punch__date = today, user=get_user).exists():
                                    err="punch in first"
                                    print(err)
                                    form = AddPunch()
                                    return render(request, 'users/punch.html', {'form': form,'err':err, 'data':list(data), 'today':today, 'ip':ip})
                                else:   
                                    err="you are already punched out"
                                    print(err)
                                    form = AddPunch()
                                    return render(request, 'users/punch.html', {'form': form,'err':err, 'data':list(data), 'today':today, 'ip':ip}) 
                    else:
                        if entered_status == 'out':
                            err="punch in first"
                            print(err)
                            form = AddPunch()
                            return render(request, 'users/punch.html', {'form': form,'err':err, 'data':list(data), 'today':today, 'ip':ip})
                        else:
                            form = form.save()

            else:
                form = AddPunch()    
    return render(request, 'users/punch.html', {'form': form, 'data':list(data), 'today':today, 'ip':ip, 'err':err})






@login_required
def get_punches(request):
    peruser = Punch.objects.filter(user=request.user)
    today_in = Punch.objects.values('punch').filter(user=request.user, status="in", role_punch__date =timezone.now().date()).last()
    today_out = Punch.objects.values('punch').filter(user=request.user, status="in", role_punch__date =timezone.now().date()).last()
    print(today_in)
    print(today_out)
    return render(request, 'authentication/user_profile.html', {'peruser':list(peruser)}) 

@login_required
@allowed_user(allowed_roles=['admin','billing'])
def get_roles(request,pk):
    date = pk
    roles = Role.objects.filter(role_punch__date=pk, user = request.user)
    peruser = Punch.objects.filter(user=request.user)
    return render(request, 'authentication/user_profile.html', {'date':date ,'roles': list(roles), 'peruser':list(peruser)}) 


#gate user
@login_required
def gate_user(request): 
    if request.method == 'POST':
        user = request.user
        role = "gate"
        role_punch = datetime.now()
        data = Role.objects.create(user=user, role=role, role_punch = role_punch)
        data.save()
        return HttpResponseRedirect('/dashboard/')


#crane user
@login_required
def crane_user(request): 
    if request.method == 'POST':
        user = request.user
        role = "crane"
        role_punch = datetime.now()
        data = Role.objects.create(user=user, role=role, role_punch = role_punch)
        data.save()
        return HttpResponseRedirect('/dashboard/')




@login_required
@allowed_user(allowed_roles=['admin','billing'])
def detail_user(request,pk):
    User = get_user_model()
    user_profile = User.objects.filter(id=pk)
    other_pro = Profile.objects.filter(user_id=pk)
    peruser = Punch.objects.filter(user_id=pk).order_by("-punch")
    today = datetime.now().date()
    roles = Role.objects.filter(user_id=pk, role_punch__date =today)
    today_punch_in = Punch.objects.filter(user_id=pk, punch__date = today, status="in")
    today_punch_out = Punch.objects.filter(user_id=pk, punch__date = today, status="out")

    punch_in = Punch.objects.filter(user_id=pk, punch__date = today, status="in").last()
    punch_out = Punch.objects.filter(user_id=pk, punch__date = today, status="out").last()


    punch_in = punch_in
    punch_out = punch_out
    
    print("this is time", punch_in, punch_out)
    last_role = Role.objects.values('role').filter(user_id=pk, role_punch__date =today).last()

    context = { 'peruser':list(peruser), 
                'today':today, 
                'roles':list(roles), 
                'last_role':last_role, 
                'user_profile':list(user_profile),
                'pro':list(other_pro),
                'punch_in': list(today_punch_in),
                'punch_out': list(today_punch_out),
                'in':punch_in,
                'out': punch_out
            }
    return render(request, 'users/detail_user.html', context)


@login_required
def get__detail_roles(request,pk):
    date = pk
    roles = Role.objects.filter(role_punch__date=pk, user = request.user)
    peruser = Punch.objects.filter(user=request.user)
    return render(request, 'authentication/user_profile.html', {'date':date ,'roles': list(roles), 'peruser':list(peruser)})



def get_client_ip(request):
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = request.META.get('REMOTE_ADDR')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    print(x_forwarded_for)
    print("no")
    print(ip)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipv = s.getsockname()[0]
    print(s.getsockname()[0])

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print(local_ip)
    return render(request, 'ip.html', {'ip':ip, 'x_forwarded_for':x_forwarded_for, 'ipv': ipv, 'local_ip': local_ip})




def show_map(request):  
    #creation of map comes here + business logic
    m = folium.Map([43.748960, -79.634340], zoom_start=30)
    html = '''1st line<br>
    2nd line<br>
    3rd line'''

    iframe = folium.IFrame(html,
                        width=100,
                        height=100)

    popup = folium.Popup(iframe,
                        max_width=100)
    # test = folium.Html('<b>Hello world</b>', script=True)
    # popup = folium.Popup(test, max_width=2650)
    tile = folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = True,
        control = True
       ).add_to(m)
    # folium.RegularPolygonMarker(location=[43.748960, -79.634340], fill_color='#28166f',popup=popup, tiles = tile).add_to(m)
    folium.Marker([43.7483, -79.63469],
              popup=popup,
              icon=folium.Icon(color='green')
             ).add_to(m)
    folium.CircleMarker([43.7483, -79.63469],
                    radius=220,
                    popup='East London',
                    color='red',
                    tiles = tile
                    ).add_to(m)
    m=m._repr_html_() #updated
    context = {'my_map': m}

    return render(request, 'map/loc.html', context)