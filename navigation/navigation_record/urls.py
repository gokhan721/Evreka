from django.urls import path
from navigation_record import views

app_name = "navigation_record"

urlpatterns = [
    path('', views.NavigationRecordListView.as_view(), name="navigationrecords"),
]
