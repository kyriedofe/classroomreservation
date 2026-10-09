from django.shortcuts import render, redirect
from .models import ClassroomReservation
from .forms import ClassroomReservationForm


def classroom_reservation(request):
    classrooms = ClassroomReservation.objects.all()

    context = {
        'reservations': classrooms
    }

    return render(request, 'ClassroomReservation/classroom.html', context)


def add_classroom_reservation(request):
    if request.method == 'POST':
        form = ClassroomReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classroom_reservation')
    else:
        form = ClassroomReservationForm()

    return render(request, 'ClassroomReservation/add_classroom.html', {'form': form})