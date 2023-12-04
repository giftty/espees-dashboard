from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    admin_type = forms.ChoiceField( initial="Sub Administrator",disabled=True, choices=[('Sub Administrator','Sub Administrator'),('Main Adminstrator','Main Adminstrator')],  required=True)
    gender = forms.ChoiceField( initial="Male",choices=[('Male','Male'),('Female','Female')],  required=True)
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.admin_type = self.cleaned_data['admin_type']
        user.save()
        return user