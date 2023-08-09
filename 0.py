import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate_agency.settings')
django.setup()

from property.models import Flat

flat = Flat.objects.first()
print(type(flat.construction_year))