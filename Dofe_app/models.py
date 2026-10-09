from django.db import models

# Create your models here.
class ClassroomReservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    classroom_number = models.CharField(max_length=50)
    requester_name = models.CharField(max_length=100)
    requester_id = models.CharField(max_length=50)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    purpose = models.CharField(max_length=255)
    number_of_participants = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=[ 
            ('Pending', 'Pending'),
            ('Approved', 'Approved'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Pending'
    )

    def __str__(self):
        return self.classroom_number