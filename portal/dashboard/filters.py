import django_filters
from django_filters import DateFilter
from .models import *
from .forms import *

class Container_in_gateFilter(django_filters.FilterSet):
    # enter_date = DateFilter(field_name='enter_date', lookup_expr='gte')
    # delivery_date = DateFilter(field_name='delivery_date', lookup_expr='gte')

    class Meta:
        model = Container_in_gate
        fields=["container_number","yard_location"]
        exclude = ['enter_date','delivery_date']




class YL_searchFilter(django_filters.FilterSet):
    location = django_filters.CharFilter( lookup_expr="icontains")
    class Meta:
        model = Container_in_gate
        fields = ['container_number']
 


