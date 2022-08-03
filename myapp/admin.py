from django.contrib import admin
from .models import Contact,User,Doctor_Profile,Appointment,CancelAppointment,HealthProfile,Transaction
# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Doctor_Profile)
admin.site.register(Appointment)
admin.site.register(CancelAppointment)
admin.site.register(HealthProfile)
admin.site.register(Transaction)