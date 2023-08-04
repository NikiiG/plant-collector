from django.contrib import admin

# Register your models here.
from .models import Plant,Feeding,Soil

# Register your models here
admin.site.register(Plant)
admin.site.register(Feeding)
admin.site.register(Soil)
