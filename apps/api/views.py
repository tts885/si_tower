from django.shortcuts import render
# Create your views here.
import django_filters
from django.http import HttpResponse
from rest_framework import viewsets, filters
from apps.accounts.models import CustomUser
from apps.pms.models.Work import Work
from .serializer import UserSerializer,WorkSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django_pandas.io import read_frame ,pd
# import pandas as pd

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
        # df = read_frame(work, fieldnames=['name', 'status', 'owner', 'planStartDate', 'planEndDate','actualEndDate'])
        df = read_frame(work, fieldnames=['planEndDate','actualEndDate','status','id'])

        # # Plan期間を算出
        planMin = pd.Series(df['planEndDate']).min()
        planMax = pd.Series(df['planEndDate']).max(axis=0)
  
        # actualMin = pd.Series(df['actualEndDate']).min()
        # actualMax = pd.Series(df['actualEndDate']).max()

        # # Plan期間の日単位スケジュールを求め
        plan_calendar =pd.date_range(planMin, planMax)

        # # 日単位Plan期間DF
        df1_calendar = pd.DataFrame({'calendar':plan_calendar})
        
        # # PlanDF   
        df2_plan = pd.DataFrame({'calendar':df['planEndDate'], 'planCount':df['planEndDate']})

        # # ActualDF  
        df3_actual = pd.DataFrame({'calendar':df['actualEndDate'], 'actualCount':df['actualEndDate']})
   
        # # 計画をカレンダーへ追加✨
        df1_addPlan = pd.merge(df1_calendar, df2_plan, on='calendar', how='outer')

        # # Date型フォーマット統一
        df1_addPlan['calendar'] =  pd.to_datetime(df1_addPlan['calendar']).dt.strftime('%Y-%m-%d')
        df3_actual['calendar'] =  pd.to_datetime(df3_actual['calendar']).dt.strftime('%Y-%m-%d')

        # # 計画を日単位でグルーピングして件数累計
        df1_addPlan = df1_addPlan.groupby(['calendar'])['planCount'].agg("count").reset_index()
        df1_addPlan['planCount'] =df1_addPlan['planCount'].cumsum()
 
        # # 実積を日単位でグルーピングして件数累計
        df3_actual = df3_actual.groupby(['calendar'])['actualCount'].agg("count").reset_index()

        # # 実績をカレンダーへ追加✨
        df1_addActual = pd.merge(df1_addPlan,df3_actual, on='calendar', how='outer').fillna(0)

        # # 実績を累計
        df1_addActual['actualCount'] = df1_addActual['actualCount'].cumsum()

        # # ===Work件数の集計=== #
        total_work = df['id'].count()

        # # ===ステータス単位件数の集計=== #
        # count_status = df[['name','status']].groupby('status').count()
        # # print(count_status.name.index)

        data = {
                "labels": df1_addActual,
                "total_work":total_work
                # "labels":jsondata,
                # "mdf":mdf.fillna(0),
                # "df6":df6.fillna(0)
                # "df1":sales_record.to_json()
                # "sales_record1":sales_record1
                # "count_status":count_status
                # "chartLabel":chartLabel,
                # "chartdata":chartdata,
                # "total_work":total_work,
                # "status":count_status.name.index,
                # "count_status":count_status.name,
                # "planEndDate":count_plan.name.index,
                # "count_plan" :count_plan.name,
                # "sumplan" :sumplan,
                # "actualEndDate" :count_actual.name.index,
                # "sumactual":sumactual,
                # "sales_record":df2['birth']
               }

        return Response(data)