from django.shortcuts import render
from main.models import Request, Client, Medicament, Pharmacy
from main.forms import ClientForm

# Create your views here.

def dashboard(request):

    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            form = ClientForm()
    else:
        form = ClientForm()

    requests = Request.objects.all()
    clients = Client.objects.all()
    medicaments = Medicament.objects.all()
    pharmacies = Pharmacy.objects.all()
    
    items = {
        'requests' : requests,
        'clients' : clients,
        'medicaments' : medicaments,
        'pharmacies' : pharmacies,
        'form': form,
    }
    return render(request, 'main/index.html', items, )
