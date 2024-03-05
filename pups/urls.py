from django.urls import path
from .views import PupList, PupDetail

urlpatterns = [
    path("", PupList.as_view(), name="pup_list"),
    path("<int:pk>/", PupDetail.as_view(), name="pup_detail"),
]
