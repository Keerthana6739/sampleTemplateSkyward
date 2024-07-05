from django.urls import path,include
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('users',users,name='users'),
    path('ref',ref,name='ref'),
    path('tc',tc,name='tc'),
    path('manifest',manifest,name='manifest'),
    path('sms',sms,name='sms'),
    path('booking',booking,name='booking'),
    path('service',service,name='service'),
    path('createuser',createuser,name='createuser'),
    path('permission',permission,name='permission'),
    path('operationcreate',operationcreate,name='opeartioncreate'),
    path('serviceload',serviceload,name='serviceload'),
    path('aircraft',aircraft,name='aircraft'),
    path('savedroutes',savedroutes,name='savedroutes'),
    path('dstnotifications',dstnotifications,name='dstnotifications'),
    path('dstrestrict',dstrestrict,name='dstrestrict'),
    path('dsttimeaddon',dsttimeaddon,name='dsttimeaddon'),
    path('acavailability',acavailability,name='acavailability'),
    path('acavailabilitytype',acavailabilitytype,name='acavailabilitytype'),
    path('ssr',ssr,name='ssr'),
    path('queues',queues,name='queues'),
    path('destination',destination,name='destination'),
    path('createpage',createpage,name='createpage'),
    path('edit',edit,name='edit'),
    
  
  



]