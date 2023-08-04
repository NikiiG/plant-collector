from django.shortcuts import render, redirect
from .models import Plant, Soil
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def plants_index(request):
    plants = Plant.objects.all()
    return render(request, "plants/index.html", {"plants": plants})


def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    id_list = plant.soils.all().values_list('id')
    soils_plant_doesnt_have = Soil.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(
        request, "plants/detail.html", {"plant": plant, "feeding_form": feeding_form,'soils': soils_plant_doesnt_have}
    )


def add_feeding(request, plant_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.plant_id = plant_id
        new_feeding.save()
    return redirect("detail", plant_id=plant_id)


class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'description', 'size', 'category']


class PlantUpdate(UpdateView):
    model = Plant
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ["description", "category", "size"]


class PlantDelete(DeleteView):
    model = Plant
    success_url = "/plants"

class SoilList(ListView):
  model = Soil

class SoilDetail(DetailView):
  model = Soil

class SoilCreate(CreateView):
  model = Soil
  fields = '__all__'

class SoilUpdate(UpdateView):
  model = Soil
  fields = ['soil_type', 'benefit']

class SoilDelete(DeleteView):
  model = Soil
  success_url = '/soils'

def assoc_soil(request, plant_id, soil_id):
  Plant.objects.get(id=plant_id).soils.add(soil_id)
  return redirect('detail', plant_id=plant_id)

def unassoc_soil(request, plant_id, soil_id):
  Plant.objects.get(id=plant_id).soils.remove(soil_id)
  return redirect('detail', plant_id=plant_id)



