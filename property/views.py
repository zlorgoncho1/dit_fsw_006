from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Property
from .forms import PropertyForm
from django.contrib.auth.decorators import login_required

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


@login_required(login_url='/account/login')
def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('properties')
    else:
        form = PropertyForm()
    return render(request, 'property/create_property.html', context={'form': form})

    form = PropertyForm()
    return render(request, 'property/create_property.html', context={'form': form})

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
