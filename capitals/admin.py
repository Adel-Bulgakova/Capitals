from django.contrib import admin
from capitals.models import Capital

class CapitalAdmin(admin.ModelAdmin):
	list_display=('question', 'answer', 'lat', 'lng')
	
admin.site.register(Capital, CapitalAdmin)