
import json
from django.shortcuts import redirect, render,HttpResponse
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import PasswordChangeView, PasswordSetView
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.urls import reverse_lazy
from asgiref.sync import sync_to_async
import requests
from django.views.decorators.csrf import csrf_exempt

from users.models import User

@csrf_exempt
def checkbalance(request,innercall=False) :
   url = "https://api.espees.org/user/espeebalance"
   payload = json.dumps({
      "username":request.POST['value']
    })
   headers = {
      'Content-Type': 'application/json'
    }
   response = requests.request("POST", url, headers=headers, data=payload)
   if innercall :
      print(response.text)
      return  response.text
   else :  
     return HttpResponse(content=response.text) 
   
@csrf_exempt   
def gettransactons(request) :
  url = "https://api.espees.org/transfer/transactions"

  payload = json.dumps({
    "wallet_address": request.POST['value']
  })
  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  return HttpResponse(content=response.text)
 

@csrf_exempt
def getwalletaddress(request) :
    url = "https://api.espees.org/user/address"
    payload = json.dumps({
      "username": request.POST['value']
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    
    data=  json.loads(checkbalance(request,True))
    res= json.loads(response.text)
    res['balance']=data['balance']
    print(res)
    return HttpResponse(content=str(res))

def createUser(request):
      user=request.user
      try:
       if(user.is_superuser==True):
         creatu= User.objects.create_user(email=request.POST['email'],password=request.POST['password'],
         username=request.POST['username'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],
         phone="no phone",gender=request.POST['gender'],admin_type=request.POST['admintype'])
       if(creatu): return HttpResponse(f'{request.POST["admintype"]} Admin created')
       else :  
        return HttpResponse('An error occurred')
      except: return HttpResponse('An error occurred')
def viewUsers(request):
      user=request.user
     # print(User.objects.all)  

def deleteUser(request):
      user=request.user
      deldata=request.POST['email']
      if(user.is_superuser == True):
         ad = User.objects.filter(email=deldata)
         print(ad)
         ad.delete()
         return HttpResponse("Delete successful")
      
class Agents(View) :
      def get(self, request):
        user = request.user 
        if(user.admin_type == "Main Admin"):
          return render(request,'menu/agents.html')
        else:
          redirect('/')
class Merchants(View) : 
        def get(self, request): 
          greeting = {}
          greeting['title'] = "Dashboard"
          greeting['pageview'] = "Espees"
          user = request.user 
          if(user.admin_type == "Main Admin"):
            return render(request,'menu/merchants.html',greeting)
          else:
            redirect('/')
class Superpageview(View):
 def get(self, request):
        greeting = {}
        greeting['title'] = "Dashboard"
        greeting['pageview'] = "Espees"
        user = request.user 
        if(user.is_superuser==True):
          return render(request,'menu/superpage.html',greeting)
        else:
          redirect('/')
 
class Mainpageview(View):
 def get(self, request):
        greeting = {}
        greeting['title'] = "Dashboard"
        greeting['pageview'] = "Espees" 
        return render(request,'menu/index.html',greeting)
# Dashboard
class DashboardView(LoginRequiredMixin,View):
       def get(self, request):
        
        dashboard_data = {}
        dashboard_data['title'] = "Dashboard"
        dashboard_data['pageview'] = "Espees" 
        user = request.user
        if(user.is_superuser == True):
          alladmins= list((User.objects.values()))
          dashboard_data['admins'] = alladmins
          return  render(request, 'menu/superpage.html',dashboard_data) 
        else:     
         if(user.admin_type == "Sub Admin"):
            dashboard_data['userprofile']={}
            return  render(request, 'menu/sub_dashboard.html',dashboard_data) 
         else :
          if(user.admin_type == "Main Admin"): 
             totalobjects=  requests.get('https://api.espees.org/backoffice/dashboard/')  
             dashboard_data['totals']= totalobjects.json()
             return render(request, 'menu/main_dashboard.html',dashboard_data)

# Calender
class CalendarView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Calendar"
        greeting['pageview'] = "Nazox"        
        return render(request, 'menu/calendar.html',greeting)

# Chat
class ChatView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Chat"
        greeting['pageview'] = "Nazox"        
        return render(request, 'menu/apps-chat.html',greeting)

# Kanban Board
class KanbanBoardView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Kanban Board"
        greeting['pageview'] = "Nazox"        
        return render(request, 'menu/apps-kanban-board.html',greeting)
    
class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy("dashboard")


class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy("dashboard")

    
    
class SettingsView(LoginRequiredMixin,View):
    def get(self, request):
        k = TOTPDevice.objects.filter(user=request.user)
        context_data = {"k": k}
        return render(request, 'menu/settings.html',context_data)