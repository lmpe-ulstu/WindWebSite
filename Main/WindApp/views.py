from django.shortcuts import render
from .influxManager import getDataByTime

from Main.settings import BUCKET
from Main.settings import URL
from Main.settings import TOKEN
from Main.settings import ORGANIZATION


def index(request):
    data = getDataByTime(BUCKET,
                         URL,
                         TOKEN,
                         ORGANIZATION)
    context = {"Weather": data}
    return render(request, 'WindApp/index.html', context)
