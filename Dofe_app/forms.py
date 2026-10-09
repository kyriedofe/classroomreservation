from django import forms
from .models import ClassroomReservation

class ClassroomReservationForm(forms.ModelForm):
    class Meta:
        model = ClassroomReservation
        fields = [
            'classroom_number',
            'requester_name',
            'requester_id',
            'date',
            'start_time',
            'end_time',
            'purpose',
            'number_of_participants',
            'status',
        ]
        widgets = {
            'classroom_number': forms.TextInput(attrs={'class': 'form-control'}),
            'requester_name': forms.TextInput(attrs={'class': 'form-control'}),
            'requester_id': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_participants': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }