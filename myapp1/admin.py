from django.contrib import admin

from myapp1.models import Patient , Donor

class PatientAdmin(admin.ModelAdmin):
    list_display = ['p_name','p_group_blood','p_unit','p_age','p_phone_no','p_email','p_date']

# Register your models here.
admin.site.register(Patient,PatientAdmin)

class DonorAdmin(admin.ModelAdmin):
    list_display = ['d_name1','d_group_blood1','d_unit1','d_age1','d_phone_no1','d_email1','d_date1']

admin.site.register(Donor,DonorAdmin)



