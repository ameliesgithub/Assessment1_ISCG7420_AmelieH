from django.urls import path, include

from appointments.views import slot_list, book_appointment, index, doctor_list, my_appointments

urlpatterns = [
    path('', index, name='index'),
    path('slots/', slot_list, name='slot_list'),
    path('doctors/', doctor_list, name='doctor_list'),
    path('book/<int:slot_id>/', book_appointment, name='book_appointment'),
    path('my_appointments/', my_appointments, name='my_appointments'),
    path('register/', register, name='register'),
    path('accounts/', include("django.contrib.auth.urls"))

]