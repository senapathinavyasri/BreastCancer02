from django.contrib import admin
from .models import Prediction  # Now imports from models/__init__.py

admin.site.register(Prediction)

# from .models import Appointment

# admin.site.register(Appointment)