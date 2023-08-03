from django.contrib import admin
from .models import Nota
from django.views.decorators.csrf import csrf_exempt

admin.site.register(Nota)
