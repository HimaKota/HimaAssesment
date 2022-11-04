from django.shortcuts import render, redirect
from .forms import UserEntryCreationForm
from .models import UserEntry, Breed


def home(request):
    
    outputs = UserEntry.objects.all().order_by('-id')
    form = UserEntryCreationForm()
    if request.method == 'POST':
        form = UserEntryCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'home.html', {'form': form,'outputs' :outputs})

# AJAX
def load_breed(request):
    animal_id = request.GET.get('animal_id')
    breeds = Breed.objects.filter(animal_id=animal_id).all()
    return render(request, 'breed_dropdown_list_options.html', {'breeds': breeds})

def delete_item(request,id):
	url = request.META.get('HTTP_REFERER')
	delete_item = UserEntry.objects.get(id=id)
	delete_item.delete()  
	return redirect(url)