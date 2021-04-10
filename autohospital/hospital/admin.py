from django.contrib import admin
from .models import Doctor_model,Patient_model,Appointment





@admin.register(Doctor_model)
class PostAdmin(admin.ModelAdmin):
     list_display = ('full_name','email','speciality','is_active',)
     list_filter	=	('is_active','speciality',	'full_name',)
     search_fields	=	('full_name',	'speciality')
     ordering	=	('is_active','full_name')
     prepopulated_fields	=	{'slug':	('full_name',)}


@admin.register(Patient_model)
class PostAdmin(admin.ModelAdmin):
     list_display = ('full_name','email','phone','is_active',)
     list_filter	=	('is_active',	'phone',	'full_name',)
     search_fields	=	('full_name',	'phone')
     ordering	=	('is_active',	'full_name')
     prepopulated_fields	=	{'slug':	('full_name',)}


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
        list_display = ('full_name','email','phone')