from django.shortcuts import render
from django.views import View


# Starter Page
class StarterPageView(View):
    def get(self,request):
        return render(request,'pages/utility/pages-starter.html',greeting)

# Maintenance
class MaintenanceView(View):
    def get(self,request):
        return render(request,'pages/utility/pages-maintenance.html')
        
# Coming-Soon
class ComingSoonView(View):
    def get(self,request):
        return render(request,'pages/utility/pages-comingsoon.html')

# Timeline
class TimelineView(View):
    def get(self,request):
        return render(request,'pages/utility/pages-timeline.html')

# Faqs
class FaqsView(View):
    def get(self,request):
        return render(request,'pages/utility/pages-faqs.html')

# Pricing
class PricingView(View):
    def get(self,request):
        return render(request,'pages/utility/pages-pricing.html')

# Error 404
class Error404View(View):
    def get(self,request):
        return render(request,'pages/utility/pages-404.html')

# Error 500
class Error500View(View):
    def get(self,request):
        return render(request,'pages/utility/pages-500.html')
    
class LoginView(View):
    def get(self,request):
        return render(request,'pages/authentication/auth-login.html')
class RegisterView(View):
    def get(self,request):
        return render(request,'pages/authentication/auth-register.html')
class LockScreenView(View):
    def get(self,request):
        return render(request,'pages/authentication/auth-lock-screen.html')
class RecoverPwView(View):
    def get(self,request):
        return render(request,'pages/authentication/auth-recoverpw.html')