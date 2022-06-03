import os
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


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

    sample_data = {'sample': 'サンプル'}
    # return render(request, 'hello_world.html', sample_data)
    return render(request, os.path.join('pms/index.html'), sample_data)