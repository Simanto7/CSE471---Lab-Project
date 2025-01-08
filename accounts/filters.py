import django_filters
from django_filters import DateFilter

from store.models import *

class OrderFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_order", lookup_expr = 'gte')
    # end_date = DateFilter(field_name="date_order", lookup_expr = 'lte')
    class Meta:
        model = StoreOrder
        fields = '__all__'
        exclude = ['customer','complete','promo_code','date_order']

        

