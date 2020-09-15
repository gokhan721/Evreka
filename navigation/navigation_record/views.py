from django.shortcuts import render
from navigation_record.models import NavigationRecord
from django.views.generic import ListView
from django.utils import timezone
from datetime import timedelta
# Create your views here.

''' Get navigation record data that is sent in last 48 hours '''
class NavigationRecordListView(ListView):
    model = NavigationRecord
    context_object_name = "navigation_records"
    def get_queryset(self):
        filtered_time = timezone.now() - timedelta(hours=48)
        return NavigationRecord.objects.filter(created_time__gte=filtered_time)
