from django.contrib import admin
from .models import Emp , Testimonial

# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display = ('name','emp_id','phone','address','working','department')
    search_fields = ('name',)
    list_filter = ('working',)

admin.site.register(Emp,EmpAdmin)

admin.site.register(Testimonial)