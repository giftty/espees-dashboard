
import csv
import json
import os
import random
from django.http import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import PasswordChangeView, PasswordSetView
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.urls import reverse_lazy
from asgiref.sync import sync_to_async
import requests
from django.views.decorators.csrf import csrf_exempt
from nazox.models import Transactions
from nazox.settings import BASE_DIR

from users.models import User

csvfolderDir= os.path.join(BASE_DIR,'static/csvfiles' )

def transferUploadPage(request):
    return render(request,'menu/transtion_file_upload.html')

@csrf_exempt  
def transferUpload(request) :
   if request.FILES :
     jsonArray = [] 
     file_url =  handle_uploaded_file(request.FILES['xlfile'])
     #read csv file
     with open(file_url, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 
        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
        jsonArray.reverse()  
        print(jsonArray[1:10]) 
        try :
         if(True) :
          for row in jsonArray :
            trans=  Transactions(
                transaction_time = row["Transaction Time"],
                transaction_reference =  row["Transaction Reference"],
                transaction_description = row["Transaction Description"],
                linking_reference = row["Linking Reference"],
                amount = row["Amount"],
                currency =  row["Currency"],
                country =  row["Country"],
                card_country =   row["Card Country"],
                is_Nigerian_Card =   row["is Nigerian Card"],
                prev_Linking_Reference =  row["Prev Linking Reference"],
                transfer_amount = row["Transfer Amount"],
                transaction_Fee =  row["Transaction Fee"],
                fee =   row["Fee"],
                status =  row["Status"],
                reason = row["Reason"],
                account_No =   row["Account No"],
                channel =   row["Channel"],
                channel_Type =  row["Channel Type"],
                is_International  =  row["Is International"],
                mode  =  row["Mode"],
                transType  =  row["TransType"],
                settlement_Amount  =  row["Settlement Amount"],
                refund_Amount  =  row["Refund Amount"],
                gateway_Response_Code  =   row["Gateway Response Code"],
                gateway_response_Message  =  row["Gateway Response Message"],has_dispute =  row["Has Dispute"],event =  row["Event"])
                
            trans.save() 
         else :
           return  HttpResponse(content="File is too large")  
        except Exception as e :
          print(e)       
    #  print(jsonArray)
    
   more_value = 0     
   if 'more_value' in request.POST.keys()  :
      print(request.POST['more_value']  ) 
      more_value = request.POST['more_value']         
      allTrans =list(Transactions.objects.all().order_by('-transaction_time')[int(more_value):2000+int(more_value)].values())   
   else :
      allTrans =list(Transactions.objects.all().order_by('-transaction_time')[:2000].values()) 

   return  HttpResponse(json.dumps(allTrans)) 
  #  try : 
  #     handle_uploaded_file(request.FILES['xlfile'])
  #     return  HttpResponse(content='success') 
  #  except Exception as e  : 
  #     print(e)
  #     return  HttpResponse(content='An error occurred'+ str(e))
@csrf_exempt  
def sendTotals(request) :
    totalAmount= 0.0
    totalTransactionFee = 0.0 
    allTrans =list(Transactions.objects.all().values()) 
    for row in allTrans :
      totalAmount = totalAmount + float(row["amount"]) 
      totalTransactionFee = totalTransactionFee + float( row["transaction_Fee"])
    totalTransactionFee =f"{round(totalTransactionFee,2):,}"
    result = f"{round(totalAmount,2):,}"  
    dataToSend = {"total-amount":str(result),"total-transaction-fee":str(totalTransactionFee)}
    print(dataToSend)
    return  JsonResponse(data=dataToSend) 

def handle_uploaded_file(file):
    random.seed(5)
    randnumb =  str(random.randint(0, 9)*100)
    with open( csvfolderDir+"/file_csvdata_to_database.csv", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)  
    return csvfolderDir+"/file_csvdata_to_database.csv"

@csrf_exempt
def deleteFiles(request) :
   try :
    filesToDelete = json.loads(request.POST['files-to-delete'])
    print(filesToDelete)
    for itm in filesToDelete :
      if os.path.exists( csvfolderDir+'/'+itm):
        os.remove(csvfolderDir+'/'+itm)
        return HttpResponse(content="File(s) removed")
      else:
       print("File not found.")
       return HttpResponse(content="File not found")
   except Exception as error :
    print(error)
    return HttpResponse(content="File doesn't exist" + str(error))
   
@csrf_exempt
def getUploadedFiles(request) :
   try : 
    dir_list = os.listdir(csvfolderDir)
    return HttpResponse(content=str(dir_list))
   except Exception as err : 
    print(err) 
    check =   str(os.path.isdir(csvfolderDir))+str(csvfolderDir)    
    return HttpResponse(content= str(err))
   
@csrf_exempt
def changeEmailPassword(request):
  url = "https://api.espees.org/user/changeemailpass"
  #payload = "{\r\n    \"email\":\"test2@gmail.com\",\r\n    \"password\":\"12345678\"\r\n}"
  print(json.dumps({
     "email":request.POST['email'],
     "password":request.POST['password']
    }))
  payload = json.dumps({
     "email":request.POST['email'],
     "password":request.POST['password']
    })
  headers = {
    'Content-Type': 'text/plain'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)
  return  HttpResponse(content=response.text)

@csrf_exempt
def changePin(request):
  url = "https://api.espees.org/resetpin"
  #payload = "{\"username\":\"firstflightboss\",\"newpin\":\"1234\"}"
  payload = json.dumps({
    "username":request.POST['username'],
    "newpin":request.POST['newpin']
  })
  headers = {
    'Content-Type': 'text/plain'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)
  return  HttpResponse(content=response.text)

def changePinAdvanced(request):
  url = "https://api.espees.org/user/newpinaddress"
  #payload = "{\"username\":\"firstflightboss\",\"newpin\":\"1234\"}"
  payload = json.dumps({
    "username":request.POST['username'],
    "new_pin":request.POST['new_pin']
  })
  headers = {
    'Content-Type': 'text/plain'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)
  return  HttpResponse(content=response.text)

@csrf_exempt
def getcarddetails(request) :
  
  url = "https://api.espees.org/cards/balance"
  #payload = "{\r\n  \"card_id\": \"0887344709917455\"\r\n}"
  payload = json.dumps({
     "card_id":request.POST['value']
    })
  headers = {
    'Content-Type': 'text/plain'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)
  return  HttpResponse(content=response.text)

@csrf_exempt
def getcardtransactions(request):
  url = "https://api.espees.org/cards/transactions"
  #payload = "{\r\n    \"card_id\":\"0887344709917455\"\r\n}"
  payload = json.dumps({
     "card_id":request.POST['value']
    })
  headers = {
    'Content-Type': 'text/plain'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)
  return  HttpResponse(content=response.text)

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

@csrf_exempt
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


 
def cardprocess(request) :
   return  render(request, 'menu/cardspage.html',{}) 

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
          else :
            banks = { "none": "Select Bank",
             "000014": "Access Bank",
             "000005": "Access (Diamond) Bank Plc",
             "100026": "Carbon",
             "000009": "Citi Bank",
             "000010": "Ecobank Nigeria",
             "000007": "Fidelity Bank Plc",
             "000016": "First Bank of Nigeria Plc",
             "000003": "First City Monument Bank(FCMB)",
             "000013": "Guaranty Trust Bank Plc",
             "000020": "Heritage Banking Company Ltd",
             "000006": "Jaiz Bank",
             "000002": "Keystone Bank Ltd",
             "090267": "Kuda Microfinance Bank",
             "090171": "Mainstreet Bank Plc",
             "090405": "Moniepoint",
             "100004": "Opay Digital Services Limited",
             "100033": "Palmpay",
             "000030": "Parallex Bank",
             "000023": "Providus Bank",
             "070011": "Refuge Montgage bank",
             "090436": "Spectrum Microfinance Bank",
             "000012": "Stanbic IBTC Plc",
             "000001": "Sterling Bank Plc",
             "000018": "Union Bank Nigeria Plc",
             "000004": "United Bank for Africa Plc",
             "000011": "Unity Bank Plc",
             "000017": "WEMA Bank Plc",
             "000015": "Zenith Bank International" 
             }
            
            for key, value in banks.items() :
               print(key)
            if(user.admin_type == "Supervisory"): 
              headers = {
                  'API-TOKEN': 'BCKOFFICE-IFHFIH973GHE35'
                }
              objects=  requests.post('http://web.espees.org/api/backoffice/outbound/parallex',headers=headers,params={})
              trn=objects.json()
              # print(trn['data'])
              dashboard_data['transactions']= trn['data']
              
                 
              return render(request, 'menu/supervisory_dashboard.html',dashboard_data)  

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