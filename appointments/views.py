from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from appointments.models import AppointmentSlot, Appointment, Doctor
from appointments.utils import create_user


# Create your views here.
def index(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')
    else:
        doctors = Doctor.objects.all()
        return render(request, 'appointments/index.html', {'doctors': doctors})
def slot_list(request):
    slots = AppointmentSlot.objects.all()
    return render(request, 'appointments/slot_list.html', {'slots': slots})

def create_slot(request):
    if not request.user.is_staff:
        return redirect('index')

    if request.method == 'POST':
        doctor_id = request.POST['doctor_id']
        date = request.POST['date']
        time = request.POST['time']

        doctor = Doctor.objects.get(id=doctor_id)

        AppointmentSlot.objects.create(doctor=doctor, date=date, time=time)

        return redirect('slot_list')

    return render(request, 'appointments/create_slot.html', {'doctors': Doctor.objects.all()})

def edit_slot(request, slot_id):
    if not request.user.is_staff:
        return redirect('index')

    slot = AppointmentSlot.objects.get(id=slot_id)

    if request.method == 'POST':
        slot.doctor = Doctor.objects.get(id=request.POST['doctor_id'])
        slot.date = request.POST['date']
        slot.time = request.POST['time']
        slot.save()

        return redirect('slot_list')

    return render(request, 'appointments/edit_slot.html', {'slot': slot, "doctors": Doctor.objects.all()})

def delete_slot(request, slot_id):
    if not request.user.is_staff:
        return redirect('index')

    slot = AppointmentSlot.objects.get(id=slot_id)
    slot.delete()
    return redirect('slot_list')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'appointments/doctor_list.html', {'doctors': doctors})

def my_appointments(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.user.is_staff:
        appointments = Appointment.objects.all()
    else:
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

def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('index')

    return render(request, 'appointments/admin_dashboard.html')

def create_doctor(request):
    if not request.user.is_staff:
        return redirect('index')

    if request.method == 'POST':
        name = request.POST['name']
        speciality = request.POST['speciality']
        Doctor.objects.create(name=name, speciality=speciality)
        return redirect('doctor_list')

    return render(request, 'appointments/create_doctor.html')

def edit_doctor(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)

    if request.method == 'POST':
        doctor.name = request.POST['name']
        doctor.speciality = request.POST['speciality']
        doctor.save()
        return redirect('doctor_list')

    return render(request, 'appointments/edit_doctor.html', {'doctor': doctor})

def delete_doctor(request, doctor_id):
    if not request.user.is_staff:
        return redirect('index')

    doctor = Doctor.objects.get(doctor_id=doctor_id)
    doctor.delete()
    return redirect('doctor_list')

def user_list(request):
    if not request.user.is_staff:
        return redirect('index')

    users = User.objects.all()
    return render(request, 'appointments/user_list.html', {'users': users})

def edit_user(request, user_id):
    if not request.user.is_staff:
        return redirect('index')

    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('user_list')

    return render(request, 'appointments/edit_user.html', {'user': user})

def delete_user(request, user_id):
    if not request.user.is_staff:
        return redirect('index')

    user = User.objects.get(id=user_id)
    if user == request.user:
        return redirect('user_list')
    else:
        user.delete()
    return redirect('user_list')