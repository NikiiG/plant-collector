from django.shortcuts import render

#plant list
plants = [
   {'name':'Neem',
          'description':'fast-growing tree of the mahogany family (Meliaceae), valued as a medicinal plant, as a source of organic pesticides, and for its timber.',
          'size': 30,
          'category':'Tree'},
          {'name':'Rose',
          'description':'A rose is either a woody perennial flowering plant of the genus Rosa in the family Rosaceae or the flower it bears.',
          'size': 1.25,
          'category':'Shrubs'},
          ]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', {
    'plants': plants
  })