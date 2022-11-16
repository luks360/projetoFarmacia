from django.shortcuts import render
from main.models import Request, Client, Medicament, Pharmacy

# Create your views here.

def dashboard(request):
    
    requests = Request.objects.all()
    clients = Client.objects.all()
    medicaments = Medicament.objects.all()
    pharmacies = Pharmacy.objects.all()
    
    items = {
        'requests' : requests,
        'clients' : clients,
        'medicaments' : medicaments,
        'pharmacies' : pharmacies,
    }
    return render(request, 'main/index.html', items, )