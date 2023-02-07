
from django.contrib import admin
from .models import *
#class ItemAdmin(admin.ModelAdmin):
 #   list_display = ('name', 'price', 'is_available')
  #  search_fields = ('name', 'price')
   # list_filter = ('is_available',)
    
admin.site.register(MenuItem)#, ItemAdmin)
