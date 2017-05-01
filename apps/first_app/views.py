# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from datetime import datetime

def index(request):

    return render(request, "first_app/index.html")

def results(request):
    print 'applesauce'
    print request.POST
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['favorite'] = request.POST['favorite']
    request.session['comment'] = request.POST['comment']
    return render(request, 'first_app/results.html')



# Create your views here.
