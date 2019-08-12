from django.shortcuts import render, HttpResponse, redirect

from datetime import datetime

def index(request):
    dateTimeObj = datetime.now()
    context = {
        "time": dateTimeObj.strftime("%I:%M %p"),
        "date": dateTimeObj.strftime("%B %d, %Y")
    }
    return render(request, 'cur_time_and_date/index.html', context)