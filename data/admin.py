from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "phone", "position", "shift", "employment_date")

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "phone", "email", "registered_date", "address")

@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ("drug_name", "supply_unit", "date_recorded")

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("patient", "prescribed_on", "prescription_notes")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "description", "date_requested", "approved")

@admin.register(PatientVisit)
class PatientVisitAdmin(admin.ModelAdmin):
    list_display = ("patient", "visit_date")

@admin.register(PatientFeedback)
class PatientFeedbackAdmin(admin.ModelAdmin):
    list_display = ("patient", "comment", "date_commented")

@admin.register(HealthHistory)
class HealthHistoryAdmin(admin.ModelAdmin):
    list_display = ("patient", "history", "diagnosis")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("drug", "date_ordered", "quantity", "status")


admin.site.site_title = "MEXICO RURAL HEALTH UNIT"
admin.site.site_header = "MEXICO RURAL HEALTH UNIT"