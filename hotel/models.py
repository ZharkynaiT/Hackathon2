from django.db import models
from django.conf import settings


class Room(models.Model):
    ROOM_CATEGORIES = (
        ('L', 'LUXE'),
        ('K', 'KING'),
        ('Q', 'QUEEN'),
        ('E', 'ECONOMY')
    )
    room_num = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.room_num}. {self.category} with {self.beds} beds for {self.capacity} people'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in_date} to {self.check_out_date}'


