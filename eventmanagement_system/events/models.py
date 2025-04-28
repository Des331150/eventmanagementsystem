from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Event(models.Model):
    """
    Model representing an event with its details like title,description,location and timing.
    """
    title = models.CharField(max_length=240)
    description = models.TextField(null=False, blank=False)
    location = models.TextField(null=False, blank=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class Registration(models.Model):
    """Model representing a user's registration to a specific event, including personal contact details.
    """
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?\d{10,15}$')])
    linked_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} registered for {self.linked_event}"