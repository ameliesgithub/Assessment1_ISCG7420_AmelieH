from django.urls import path, include

from appointments.views import slot_list, book_appointment, index, doctor_list, my_appointments, register, \
    cancel_appointment, edit_appointment, admin_dashboard, create_doctor, edit_doctor, delete_doctor, user_list, \
    edit_user, delete_user, edit_slot, delete_slot, create_slot

urlpatterns = [
    path('', index, name='index'),
    path('slots/', slot_list, name='slot_list'),
    path('doctors/', doctor_list, name='doctor_list'),
    path('book/<int:slot_id>/', book_appointment, name='book_appointment'),
    path('my_appointments/', my_appointments, name='my_appointments'),
    path('cancel_appointment/<int:appointment_id>/', cancel_appointment, name='cancel_appointment'),
    path('edit_appointment/<int:appointment_id>/', edit_appointment, name='edit_appointment'),
    path('register/', register, name='register'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('create_doctor/', create_doctor, name='create_doctor'),
    path('edit_doctor/<int:doctor_id>/', edit_doctor, name='edit_doctor'),
    path('delete_doctor/<int:doctor_id>/', delete_doctor, name='delete_doctor'),
    path('user_list/', user_list, name='user_list'),
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('edit_slot/<int:slot_id>/', edit_slot, name='edit_slot'),
    path('delete_slot/<int:slot_id>/', delete_slot, name='delete_slot'),
    path('create_slot/', create_slot, name='create_slot')

]