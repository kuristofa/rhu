from django.urls import path
from . import views

urlpatterns =  [
    #view
    path("", views.home, name="homepage"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("patients/", views.patients, name="patients"),
    path("staff/", views.staffs, name="staff"),
    path("prescriptions/", views.prescriptions, name="prescriptions"),
    path("drugs/", views.drugs, name="drugs"),
    path("feedbacks/", views.feedback, name="feedbacks"),
    path("health_histories/", views.health_histories, name="health_histories"),
    path("appointments/", views.appointments, name="appointments"),
    path("visits/", views.visits, name="visits"),
    path("order_form/", views.order_form, name="order_form"),
    path("add_order/", views.add_order, name="add_order"),


    #authenticaiton
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),

    #data insert
    path("add_appointment/", views.add_appointment, name="add_appointment"),
    path("add_drug/", views.add_drug, name="add_drug"),
    path("add_feedback/", views.add_feedback, name="add_feedback"),
    path("add_health_history/", views.add_health_history, name="add_health_history"),
    path("add_patient/", views.add_patient, name="add_patient"),
    path("add_prescription/", views.add_prescription, name="add_prescription"),
    path("add_staff/", views.add_staff, name="add_staff"),
    path("add_visit/", views.add_visit, name="add_visit"),

    #view details
    path("patient_details/<int:id>/", views.patient_details, name="patient_details"),
    path("prescription_details/<int:id>/", views.prescription_details, name="prescription_details"),
    path("staff_details/<int:id>/", views.staff_details, name="staff_details"),
    path("drug_details/<int:id>/", views.drug_details, name="drug_details"),
    path("appointment_details/<int:id>/", views.appointment_details, name="appointment_details"),

    #edit details
    path("edit_appointment/<int:id>/", views.add_appointment, name="edit_appointment"),
    path("edit_drug/<int:id>/", views.add_drug, name="edit_drug"),
    path("edit_patient/<int:id>/", views.add_patient, name="edit_patient"),
    path("edit_health_history/<int:id>/", views.add_health_history, name="edit_health_history"),
    path("edit_staff/<int:id>/", views.add_staff, name="edit_staff"),
    path("edit_visit/<int:id>/", views.add_visit, name="edit_visit"),
    path("edit_prescription/<int:id>/", views.add_prescription, name="edit_prescription"),
    path("edit_feedback/<int:id>/", views.add_feedback, name="edit_feedback"),
]