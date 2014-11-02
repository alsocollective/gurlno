from django.contrib import admin
from galleries.models import *
# Register your models here.
admin.site.register(Gallery)
admin.site.register(artType)
admin.site.register(Event)
admin.site.register(WorkMedium)
admin.site.register(Artist)
admin.site.register(WorkImage)