from django.contrib import admin
from .models import item
class itemUserAdmin(admin.ModelAdmin):
	Search_field = ["name"]
	class Meta:
		model = item
admin.site.register(item, itemUserAdmin)