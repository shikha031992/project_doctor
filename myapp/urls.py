from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('gallery/',views.gallery,name='gallery'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('contact/',views.contact,name='contact'),
    path('logout/',views.logout,name='logout'),
    path('doctor_index/',views.doctor_index,name='doctor_index'),
    path('doctor_profile/',views.doctor_profile,name='doctor_profile'),
    path('doctors/',views.doctors,name='doctors'),
    path('doctor_detail/<int:pk>/',views.doctor_detail,name='doctor_detail'),
    path('book_appointment/<int:pk>/',views.book_appointment,name='book_appointment'),
    path('myappointment/',views.myappointment,name='myappointment'),
    path('patient_cancel_appointment/<int:pk>/',views.patient_cancel_appointment,name='patient_cancel_appointment'),
    path('change_password/',views.change_password,name='change_password'),
    path('health_profile/',views.health_profile,name='health_profile'),
    path('doctor_appointment/',views.doctor_appointment,name='doctor_appointment'),
    path('doctor_approve_appointment/<int:pk>/',views.doctor_approve_appointment,name='doctor_approve_appointment'),
    path('doctor_complete_appointment/<int:pk>/',views.doctor_complete_appointment,name='doctor_complete_appointment'),
    path('doctor_cancel_appointment/<int:pk>/',views.doctor_cancel_appointment,name='doctor_cancel_appointment'),
    path('payment/',views.initiate_payment, name='payment'),
    path('callback/',views.callback, name='callback'),
    path('ajax/validate_email/',views.validate_email,name='validate_email'),
]