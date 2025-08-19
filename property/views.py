from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Property
from .forms import PropertyForm
from django.contrib.auth.decorators import login_required
from django.views import View

def welcome(request):
    return render(request, 'index.html')

def properties(request):
    sectionTitle = "Propriétés en vedette"
    properties = Property.objects.all()
    return render(request, 'property/properties.html', context={'properties': properties, 'title': sectionTitle})

def property_detail(request, property_id):
    property = Property.objects.filter(id=property_id).first()
    if property:
        return render(request, 'property/property_detail.html', context={'property': property})
    else:
        return HttpResponse(f"Propriété non trouvée avec l'ID {property_id}")


class PropertyView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/account/login')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        form = PropertyForm()
        return render(request, 'property/create_property.html', context={'form': form})

    def post(self, request):
        form = PropertyForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('properties')
        else:
            return render(request, 'property/create_property.html', context={'form': form})
    
    
def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
