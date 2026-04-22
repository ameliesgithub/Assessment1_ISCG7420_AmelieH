from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from appointments.models import AppointmentSlot, Appointment, Doctor
from appointments.utils import create_user


# Create your views here.
def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'appointments/index.html', {'doctors': doctors})
def slot_list(request):
    slots = AppointmentSlot.objects.all()
    return render(request, 'appointments/slot_list.html', {'slots': slots})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'appointments/doctor_list.html', {'doctors': doctors})

def my_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointments/my_appointments.html', {'appointments': appointments})

def book_appointment(request, slot_id):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        Appointment.objects.create(user=request.user, slot=AppointmentSlot.objects.get(id=slot_id))
        return redirect('my_appointments')

    return render(request, 'appointments/book_appointment.html', {'slot': AppointmentSlot.objects.get(id=slot_id)})

def cancel_appointment(request, slot_id):
    Appointment.objects.filter(user=request.user, slot=AppointmentSlot.objects.get(id=slot_id)).delete()
    return redirect('my_appointments')

def edit_appointment(request, slot_id):
    return render(request, 'appointments/edit_appointment.html', {'slot': AppointmentSlot.objects.get(id=slot_id)})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        create_user(username, password, first_name, last_name, email)

        return redirect('login')
    return render(request, 'registration/register.html')
