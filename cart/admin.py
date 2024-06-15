from django.contrib import admin
from .models import Cotegory, Product, Cart


admin.site.register([Cotegory, Product, Cart])