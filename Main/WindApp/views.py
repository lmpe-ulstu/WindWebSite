from django.http import HttpResponse
from django.shortcuts import render
from .influxManager import getDataByTime

from .config import BUCKET
from .config import URL
from .config import TOKEN
from .config import ORGANIZATION


def index(request):
    data = getDataByTime(BUCKET,
                         URL,
                         TOKEN,
                         ORGANIZATION)
    context = {"Weather": data}
    return render(request, 'WindApp/index.html', context)
