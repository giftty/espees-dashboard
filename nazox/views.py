
from django.shortcuts import redirect, render,HttpResponse
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import PasswordChangeView, PasswordSetView
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.urls import reverse_lazy

from users.models import User

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
      print(User.objects.all)  

def deleteUser(request):
      user=request.user
      deldata=request.POST['email']
      if(user.is_superuser == True):
         data = User.objects.get(pk=2)
         print(data)
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
        
        greeting = {}
        greeting['title'] = "Dashboard"
        greeting['pageview'] = "Espees" 
        user = request.user
        if(user.is_superuser == True):
          alladmins= list((User.objects.values()))
          greeting['admins'] = alladmins
          #print(greeting['admins']) 
          return  render(request, 'menu/superpage.html',greeting) 
        else:     
         if(user.admin_type == "Sub Admin"):
           # print(user.admin_type)
            return  render(request, 'menu/sub_dashboard.html',greeting) 
         else :
          if(user.admin_type == "Main Admin"):     
             return render(request, 'menu/main_dashboard.html',greeting)

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