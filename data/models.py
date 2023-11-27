from django.db import models
from django.utils import timezone

# Create your models here.
SEX_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)
SHIFT_CHOICES = (
    ("Day", "Day"),
    ("Afternoon", "Afternoon"),
)
STAFF_CHOICES = (
    ("Nurse", "Nurse"),
    ("Clinical Officer", "Clinical Officer"),
    ("Public Health Officer", "Public Health Officer"),
    ("Cleaner", "Cleaner"),
    ("Security", "Security"),
    ("Driver", "Driver"),
    ("Counselor", "Counselor"),
    ("Nutritionist", "Nutritionist"),
    ("Doctor", "Doctor"),
)
STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("Approved", "Approved"),
)

STATUS_UPDATE = (
    ("RHU", "RHU"),
    ("Referred to MCH", "Referred to MCH")
)


class BaseInfo(models.Model):
    id_number = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=SEX_CHOICES)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)

    class Meta:
        abstract = True

class Staff(BaseInfo):
    position = models.CharField(max_length=100, choices=STAFF_CHOICES)
    employment_date = models.DateTimeField()
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)

    def __str__(self):
        return self.name

class Patient(BaseInfo):
    registered_date = models.DateTimeField(default=timezone.now)
    status_update = models.CharField(max_length=50, choices=STATUS_UPDATE, default='RHU')
    
    def get_barangay (self):
        address_parts = self.address.split(',')
        barangay_index = 2

        if len(address_parts) > barangay_index:
            barangay = address_parts[barangay_index].strip().lower()
        
            if barangay.endswith('mexico') and 'pampanga' in barangay:
                barangay = barangay.replace('mexico', '').replace('pampanga', '').strip(', ').title()
             
            return barangay
        
        return None

    def __str__(self):
        return self.name

CONTRACT_CHOICES = (
    ("Temporary", "Temporary"),
    ("Permanent", "Permanent"),
)

class Drug(models.Model):
    drug_name = models.CharField(max_length=500)
    supplied_on = models.DateTimeField(default=timezone.now)
    supply_unit = models.CharField(max_length=300)
    date_recorded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.drug_name

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescribed_on = models.DateTimeField(default=timezone.now)
    prescription_notes = models.TextField()

    def __str__(self):
        return self.patient.name + " " + str(self.prescribed_drug)
    
class Order(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField(default=1)  # You might want to change this field depending on how you want to track quantities.
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pending' )  # Default status set to 'Pending'

    def __str__(self):
        return f"Order for {self.drug.drug_name} - Status: {self.status}"

class Appointment(models.Model):
    id_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=SEX_CHOICES)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    description = models.TextField(null=True)
    date_requested = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class PatientVisit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name

class PatientFeedback(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    comment = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name
    
class HealthHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    history = models.TextField()
    diagnosis = models.TextField(null=True)

    def __str__(self):
        return self.patient.name