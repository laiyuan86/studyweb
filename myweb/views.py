from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from .dbhelp import execmysql
import time
import json
import os
import csv

from .config import *

# Create your views here.


def index(request):
    exmysql = execmysql(host, user, password, db)
    setimes = []
    rectime = request.GET.items()
    for i in rectime:
        setimes.append(i[1])
    if setimes:
        if setimes[0]:
            nums = exmysql.get_events_nums_date(*setimes)
        else:
            nums = exmysql.get_events_nums()
    else:
        nums = exmysql.get_events_nums()
    data = {
        'name': '本周工作量',
        'data': nums
    }
    json_data = json.dumps(data, separators=(',', ':'))
    ips = exmysql.search_data()[1]

    return render(request, 'myweb/index.html', {'series': json_data, 'ips': ips})


def about(request):
    return render(request, 'myweb/about.html')


def news(request):
    return render(request, 'myweb/creatvms.html')


def add_event(request):
    exmysql = execmysql(host, user, password, db)
    ips = exmysql.search_data()[1]
    return render(request, 'myweb/add.html', {'ips': ips})


def insertdata(request):
    cvminfo = []
    res = request.GET.items()
    for i in res:
        cvminfo.append(i[1])
    exmysql = execmysql(host, user, password, db)
    exmysql.insert_data(cvminfo[0], cvminfo[1], cvminfo[2], cvminfo[3], cvminfo[4], cvminfo[5], cvminfo[6])
    return HttpResponseRedirect('/')


def get_cvms_info(request):
    vmsinfo = execmysql(host, user, password, db).search_data()[0]
    return render(request, "myweb/creatvms.html", {'vmsinfo': vmsinfo})


def get_hight_info(request):
    data = {
        'name': '本周工作量',
        'data': [
            80,
            40,
            20
        ]
    }
    json_data = json.dumps(data, separators=(',', ':'))
    return render(request, "myweb/highchart.html", {'series': json_data})


def insert_deal_event(request):
    deal_event = []
    res = request.GET.items()
    for i in res:
        deal_event.append(i[1])
    exmysql = execmysql(host, user, password, db)
    exmysql.insert_deal_event(deal_event[0], deal_event[2], deal_event[1])
    return HttpResponseRedirect('/')


def insert_vmchange(request):
    vmchange = []
    res = request.GET.items()
    for i in res:
        vmchange.append(i[1])
    exmysql = execmysql(host, user, password, db)
    exmysql.insert_vmchange(vmchange[0], vmchange[2], vmchange[1])
    return HttpResponseRedirect('/')


@csrf_protect
def get_files(request):
    if request.method == 'POST':
        ret = {'status': False, 'data': None, 'error': None}
        try:
            rcfile = request.FILES.get('uploadfile')
            f = open(os.path.join('static', rcfile.name), 'wb')
            for chunk in rcfile.chunks(chunk_size=1024):
                print(chunk)
                f.write(chunk)
            ret['status'] = True
            ret['data'] = os.path.join('static', rcfile.name)
        except Exception as e:
            ret['error'] = e
        finally:
            f.close()
            csv_file = csv.reader(open(os.path.join('static', rcfile.name), 'r'))
            print(csv_file)
            exmysql = execmysql(host, user, password, db)
            for vminfo in csv_file:
                print(vminfo)
                exmysql.insert_data(vminfo[0], vminfo[1], vminfo[2], vminfo[3], vminfo[4], vminfo[5], vminfo[6] )
            return HttpResponseRedirect('/vmsinfo/')
    return render(request, 'myweb/add.html')


def table_fy(request):
    return render(request, "myweb/tablefy.html")


def search_ip(request):
    ip = request.GET.get('ip')
    exmysql = execmysql(host, user, password, db)
    vminfo = exmysql.get_vminfo_forip(ip)
    return render(request, "myweb/vmdetail.html", {'vminfo': vminfo})


if __name__ == '__main__':
    pass