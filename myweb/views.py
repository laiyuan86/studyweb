from django.shortcuts import render
from django.http import HttpResponse
from .dbhelp import execmysql
import time, json

from .config import *

# Create your views here.


def index(request):
    data = {
        'name': '本周工作量',
        'data': [
            80,
            40,
            20
        ]
    }
    json_data = json.dumps(data, separators=(',', ':'))
    return render(request, 'myweb/index.html', {'series': json_data})


def about(request):
    return render(request, 'myweb/about.html')


def news(request):
    return render(request, 'myweb/creatvms.html')


def contact(request):
    return render(request, 'myweb/contact.html')


def insertdata(request):
    cvminfo = []
    res = request.GET.items()
    for i in res:
        cvminfo.append(i[1])
    exmysql = execmysql(host, user, password, db)
    exmysql.insert_data(cvminfo[0], cvminfo[1], cvminfo[2], cvminfo[3], cvminfo[4], cvminfo[5], cvminfo[6])
    return HttpResponse("<h1>提交成功</h1>")


def get_cvms_info(request):
    vmsinfo = execmysql(host, user, password, db).search_data()
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


if __name__ == '__main__':
    insertdata()
