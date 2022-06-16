from django.shortcuts import render

# Create your views here.
import django_filters

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, filters
from apps.accounts.models import CustomUser
from apps.pms.models.Work import Work
from .serializer import UserSerializer,WorkSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django_pandas.io import read_frame


def index(request):
    return HttpResponse("Hello, world.")

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):
        work = Work.objects.all()
        df = read_frame(work, fieldnames=['name', 'status', 'owner', 'planStartDate', 'planEndDate'])

        # ===Work件数の集計=== #
        total_work = df['name'].count()

        # ===ステータス単位件数の集計=== #
        count_status = df[['name','status']].groupby('status').count()
        print(count_status.name.index)

        # ===予定日単位件数=== #
        count_plan = df[['planEndDate','name']].groupby('planEndDate').count()
        print(count_plan.name.index)


        # labels = [
        #     'January',
        #     'February', 
        #     'March', 
        #     'April', 
        #     'May', 
        #     'June', 
        #     'July'
        #     ]
        labels = count_status.name.index
        chartLabel = "予定"
        chartdata = count_status.name
        data = {
                "labels":labels,
                "chartLabel":chartLabel,
                "chartdata":chartdata,
                "total_work":total_work,
                "status":count_status.name.index,
                "count_status":count_status.name,
                "planEndDate":count_plan.name.index,
                "count_plan" :count_plan
               }
        return Response(data)