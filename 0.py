import os
import django
from django.shortcuts import get_object_or_404
import phonenumbers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate_agency.settings')
django.setup()

from property.models import Flat

flat = get_object_or_404(Flat, owners_phonenumber='+70000000000')
parse_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
pure_number = phonenumbers.format_number(parse_number, phonenumbers.PhoneNumberFormat.E164)
print(pure_number)