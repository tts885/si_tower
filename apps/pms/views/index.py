import os
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from apps.pms.models.Work import Work
from django_pandas.io import read_frame


@login_required()
def demo(request):
    context = {}
    template = loader.get_template('pms/app/index.html')
    return HttpResponse(template.render(context, request))


@login_required()
def html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('pms/app/' + request.path)
    return HttpResponse(template.render(context, request))


@login_required()
def index(request):
    # context = {}
    # template = loader.get_template('pms/portal/index.html')
    # return HttpResponse(template.render(context, request))

    index_data = {'index_data': 'xxxx_data'}

    return render(request, os.path.join('pms/index.html'), index_data)

@login_required()
def dashboard(request):
    # context = {}
    # template = loader.get_template('pms/portal/index.html')
    # return HttpResponse(template.render(context, request))
    work = Work.objects.all()
    df = read_frame(work, fieldnames=['name', 'status', 'owner', 'planStartDate', 'planEndDate'])

    # ===Work件数の集計=== #
    total_work = df['name'].count()

    # count_status = df[['name','status']].groupby('status').count()

    context_data = {'total_work': ''}

    return render(request, os.path.join('pms/pm/dashboard/ dashboard.html'), context_data)