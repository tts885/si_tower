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
import pandas as pd
import random
import numpy as np
import json

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
        df = read_frame(work, fieldnames=['planEndDate','actualEndDate'])


        planMin = pd.Series(df['planEndDate']).min()
        planMax = pd.Series(df['planEndDate']).max(axis=0)
  
        actualMin = pd.Series(df['actualEndDate']).min()
        actualMax = pd.Series(df['actualEndDate']).max()

        planAll =pd.date_range(planMin, planMax)
        df1 = pd.DataFrame({'plan':planAll})
        df2 = pd.DataFrame({'plan':df['planEndDate'], 'planCount':df['planEndDate']})
        df3 = pd.DataFrame({'plan':df['actualEndDate'], 'actualCount':df['actualEndDate']})

        mdf = pd.merge(df1,df2, on='plan', how='outer')

        mdf['plan'] =  pd.to_datetime(mdf['plan']).dt.strftime('%Y-%m-%d')
        df3['plan'] =  pd.to_datetime(df3['plan']).dt.strftime('%Y-%m-%d')

        # mdf['plan'] = pd.to_datetime(mdf['plan']).dt.strftime('%Y-%m-%d')
        mdf = mdf.groupby(['plan'])['planCount'].agg("count").reset_index()
        mdf['planCount'] = mdf['planCount'].cumsum()

        df3 = df3.groupby(['plan'])['actualCount'].agg("count").reset_index()

        mdf1 = pd.merge(mdf,df3, on='plan', how='outer').fillna(0)

        # mdf1['plan'] = pd.to_datetime(mdf1['plan']).dt.strftime('%Y-%m-%d')

        # mdf1 = mdf1.groupby(['plan'])['planCount','actualCount'].agg("count").reset_index()
        # mdf1['planCount'] = mdf1['planCount'].cumsum()
        mdf1['actualCount'] = mdf1['actualCount'].cumsum()



        # mdf = mdf.groupby(['plan'])['planCount','actualCount'].agg("count").reset_index()
        # mdf['planCount'] = mdf['planCount'].cumsum()
        # mdf['actualCount'] = mdf['actualCount'].cumsum()   






        # df1 = df.groupby("planEndDate").count()
        # df1 = df.groupby(['planEndDate']).count()[("name")].reset_index()
        # df1 = df.groupby(['planEndDate'])['actualEndDate','name'].agg("count").reset_index()
        # df1['actualEndDate'] =  df1['actualEndDate'].cumsum()
        # df1['name'] =  df1['name'].cumsum()

        # # df1['planEndDate'] = pd.to_datetime(df1['planEndDate']).dt.strftime('%Y-%m-%d')



        # # 日付データの作成
        # dates=pd.date_range('2022-06-1','2022-12-31')

        # # # 売上データの作成
        # # sales1=[random.randint(100000, 300000) for i in range(240)]

        # # データフレームの作成
        # # sales_record1=pd.DataFrame({'日付':dates,
        # #                             '売上':sales1})



        # df2 = pd.DataFrame({'date': dates})
        # df3 = pd.DataFrame(df)
        # df3.groupby(df3['actualEndDate']).mean()
        # pd.Series(df3['actualEndDate']).min()



        # df2 = pd.DataFrame(data=df)

        # df2['planDate'] = np.where(df2['date'] == df['planEndDate'],df2['date'],'')
        # ----------------

        # list_of_dates = ['2019-11-20', '2020-01-02', '2020-02-05','2020-03-10','2020-04-16','2020-05-01']
        # employees = ['Hisila', 'Shristi','Zeppy','Alina','Jerry','Kevin']
        # salary = [200,400,300,500,600,300]
        # df = pd.DataFrame({"Name":employees,'Joined date': pd.to_datetime(list_of_dates),"Salary":salary})

        # conditionlist = [
        #     (df['Salary'] >= 500) 
        #     # (df['Salary'] >= 300) & (df['Salary'] <300),
        #     # (df['Salary'] <= 300)
        #     ]
        # choicelist = ['High']
        # df['Salary_Range'] = np.select(conditionlist, choicelist, default='Not Specified')


        # ----------------
        
        # sales_record['year']=sales_record['planEndDate'].dt.year
        # sales_record['month']=sales_record['planEndDate'].dt.month
        # sales_record['planEndDate'] = pd.to_datetime(sales_record['planEndDate']).dt.strftime('%Y-%m-%d')
        # sales_record['actualEndDate'] = pd.to_datetime(sales_record['actualEndDate']).dt.strftime('%Y-%m-%d')
        
        # sales_record['planEndDate'] = pd.to_datetime(sales_record['planEndDate'])
        # sales_record['actualEndDate'] = pd.to_datetime(sales_record['actualEndDate'])

        # sales_record.set_index('planEndDate', inplace=True)
        # sales_record.resample('W').sum()




        # sales_record['name'] = sales_record['name'].count()
        # sales_record.set_index('planEndDate', inplace=True)
        # sales_record.resample('W').mean()

        # count_status = sales_record.groupby('planEndDate')


        # sales_record['week']=sales_record['planEndDate'].dt.week
        # sales_record['月']=sales_record['日付'].dt.month
        # sales_record=sales_record[['年','月','日付','売上']]
        # sales_record=sales_record[['planEndDate']]



        #日付に変換
        # df['planEndDate'] = pd.to_datetime(df['planEndDate'])


        # # ===Work件数の集計=== #
        # total_work = df['name'].count()

        # # ===ステータス単位件数の集計=== #
        # count_status = df[['name','status']].groupby('status').count()
        # # print(count_status.name.index)

        # # ===予定終了日単位件数=== #
        # count_plan = df[['planEndDate','name']].groupby('planEndDate').count()
        #  # ===予定終了日単位累計=== #       
        # sumplan = count_plan.cumsum().name

        # # ===予定終了日単位件数=== #
        # count_actual = df[['actualEndDate','name']].groupby('actualEndDate').count()
        # # ===予定終了日単位累計=== #       
        # sumactual = count_actual.cumsum().name


        # # # 日付データの作成
        # # dates=pd.date_range('2020-10-01','2020-12-31')

        # # # 売上データの作成
        # # sales=[random.randint(100000, 300000) for i in range(92)]

        # # # データフレームの作成
        # # sales_record=pd.DataFrame({'日付':dates,
        # #                            '売上':sales})

        # df2 = pd.DataFrame(
        #     {'name': ['白銀', '藤原', '石上', '四宮', '早坂'], 
        #     'grade': ['3', '3', '2', '3', '3'],
        #     'height': [177, 162, 175, 160, 165],
        #     'weight': [62, 54, 60, 48, 54],
        #     'birth': ['2002/9/9', '2002/3/3', '2003/3/3', '2002/1/1', '2002/4/2']
        #     },
        #     index=[1, 2, 3, 4, 5]
        # )
        
        # #日付に変換
        # df2['birth'] = pd.to_datetime(df2['birth'])
        

        # print(count_plan)
        # labels = [
        #     'January',
        #     'February', 
        #     'March', 
        #     'April', 
        #     'May', 
        #     'June', 
        #     'July'
        #     ]
        # labels = count_status.name.index
        # chartLabel = "予定"
        # chartdata = count_status.name
        data = {
                "labels":mdf1.fillna(0),
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