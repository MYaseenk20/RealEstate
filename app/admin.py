from django.contrib import admin
from .models import Realtor,Contact,Listings
# Register your models here.
admin.site.register(Realtor)
admin.site.register(Listings)
admin.site.register(Contact)
