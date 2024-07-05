from django.shortcuts import render,redirect
from main_app.views import *
import json
from .forms import *
from django.contrib import messages
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import base64
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse #This is i am using in client contact edit for redirect to main page

from django.utils import timezone


# Create your views here.
def dashboard(request):
    return render(request, 'Administration/dashboard.html')

def users(request):
    return render(request, 'Administration/users.html')

def ref(request):
    return render(request, 'Administration/ref.html')

def tc(request):
    return render(request, 'Administration/tc.html')

def manifest(request):
    return render(request, 'Administration/manifest.html')

def sms(request):
    return render(request, 'Administration/sms.html')

def booking(request):
    return render(request, 'Administration/booking.html')

def service(request):
    return render(request, 'Administration/service.html')

def createuser(request):
    return render(request, 'Administration/createuser.html')

def permission(request):
    return render(request, 'Administration/permission.html')

def operationcreate(request):
    form=AircraftTypeForm()
    return render(request, 'OperationAdmin/operationcreate.html',{'form':form})

def serviceload(request):
    form=ServiceLoadForm()
    return render(request, 'OperationAdmin/serviceload.html',{'form':form})

def aircraft(request):
    form=AirCraftForm()
    return render(request, 'OperationAdmin/aircraft.html',{'form':form})

def savedroutes(request):
    form=SaveRouteForm()
    return render(request, 'OperationAdmin/savedroutes.html',{'form':form})

def dstnotifications(request):
    form=DSTNotificationsForm()
    return render(request, 'OperationAdmin/dstnotifications.html',{'form':form})

def dstrestrict(request):
    form=DSTRestrictForm()
    return render(request, 'OperationAdmin/dstrestrict.html',{'form':form})

def dsttimeaddon(request):
    form=DSTTimeAddonForm()
    return render(request, 'OperationAdmin/dsttimeaddon.html',{'form':form})

def acavailability(request):
    form=AcAvailabilityForm()
    return render(request, 'OperationAdmin/acavailability.html',{'form':form})

def acavailabilitytype(request):
    form=AcAvailabilityTypeForm()
    return render(request, 'OperationAdmin/acavailabilitytype.html',{'form':form})

def ssr(request):
    form=SpecialServicesForm()
    return render(request, 'OperationAdmin/ssr.html',{'form':form})

def queues(request):
    form=QueuesForm()
    return render(request, 'OperationAdmin/queues.html',{'form':form})

def destination(request):
    form=DestinationForm()
    return render(request, 'OperationAdmin/destination.html',{'form':form})

def createpage(request):
    form=DestinationForm()
    return render(request, 'OperationAdmin/createpage.html',{'form':form})

def edit(request):
    form=DestinationForm()
    return render(request, 'OperationAdmin/edit.html',{'form':form})
