from django.urls import path
from .views import DashboardView, CategoryWiseView, RecentRecordsView

urlpatterns = [
    path('summary/', DashboardView.as_view()),
    path('category-wise/', CategoryWiseView.as_view()),
    path('recent/', RecentRecordsView.as_view()),
]