from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# UI-Elements
# Alerts
class AlertsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-alerts.html')        

# Buttons
class ButtonsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-buttons.html')        

# Cards
class CardsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-cards.html')        

# Carousel
class CarouselView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-carousel.html')        

# Dropdowns
class DropdownsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-dropdowns.html')        

# Grid
class GridView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-grid.html')        

# Images
class ImagesView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-images.html')        

# Lightbox
class LightboxView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-lightbox.html')        

# Modals
class ModalsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-modals.html')        

# Offcavas
class OffcanvasView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-offcanvas.html')        

# Range Slider
class RangeSliderView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-rangeslider.html')        

# Round Slider
class RoundSliderView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-roundslider.html')        

# Session Timeout
class SessionTimeoutView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-session-timeout.html')        

# Progress Bars
class ProgressBarsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-progressbars.html')        

# Sweetalert 2
class SweetAlertView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-sweet-alert.html')        

# Tabs & Accordions
class TabsAccordionsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-tabs-accordions.html')        

# Typography
class TypographyView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-typography.html')        

# Video
class VideoView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-video.html')        

# General
class GeneralView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-general.html')        

# Rating
class RatingView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-rating.html')        

# Notifications
class NotificationsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/ui-elements/ui-notifications.html')                                                

# Forms
# Form Elements
class FormElementsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/forms/form-elements.html')        

# Form Validation
class FormValidationView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/forms/form-validation.html')        

# Form Advanced Plugin
class FormAdvancedPluginsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/forms/form-advanced.html')        

# Form Editors
class FrormEditorsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/forms/form-editors.html')        

# Form File Upload
class FormFileUploadView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/forms/form-uploads.html')        

# Form X-editable
class FormXeditableView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/forms/form-xeditable.html')        

# Form Wizard
class FormWizardView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/forms/form-wizard.html')                                                

# Form Mask
class FormMaskView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/forms/form-mask.html')        


# Tables
# Basic Table
class BasicTableView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/tables/tables-basic.html')        

# Datatables
class DatatableView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/tables/tables-datatable.html')        

# Editable
class EditableView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/tables/tables-editable.html')                                                

# Responsive Table
class ResponsiveView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/tables/tables-responsive.html')        

# Charts
# Apex Charts
class ApexView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/charts/charts-apex.html')        

# Chartjs Charts
class ChartjsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/charts/charts-chartjs.html')        

# Flot Charts
class FlotView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/charts/charts-flot.html')                                                

# Knob Charts
class KnobView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/charts/charts-knob.html') 

# Sparkline Charts
class SparklineView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/charts/charts-sparkline.html') 

# Icons
# Remix Icons
class RemixIconsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/icons/icons-remix.html')        

# Materialdesign Icons Charts
class MaterialdesignIconsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/icons/icons-materialdesign.html')                                                

# Dripicons Icons
class DripiconsIconsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/icons/icons-dripicons.html') 

# Fontawesome Icons
class FontawesomeIconsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/icons/icons-fontawesome.html') 

# Maps
# Google Maps
class GoogleMapsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/maps/maps-google.html') 

# Vector Maps
class VectorMapsView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'components/maps/maps-vector.html') 