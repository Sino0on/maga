from django.urls import path
from .views import *


urlpatterns = [
    path('tests', TestListApiView.as_view()),
    path('tests/<int:pk>', TestDetailApiView.as_view()),
    path('result/create', ResultCreateApiView.as_view()),
]