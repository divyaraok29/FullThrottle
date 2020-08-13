from django.db import models
from django.urls import reverse
import uuid


# User Model: (id, first_name, last_name)
class Users(models.Model):
    # Fields
    id = models.CharField(max_length=9, primary_key=True, default=uuid.uuid4().hex[:9].upper(), help_text='User Id - Primary Key')
    first_name = models.CharField(max_length=20, help_text='First name of the user')
    last_name = models.CharField(max_length=20, help_text='Last name of the user')

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('full-name', args=[str(self.id)])


# UserActivity Model: (activity_id, user_id, start_time, end_time)
class UserActivity(models.Model):
    # Fields
    activity_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Activity Id - Primary Key')
    user_id = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True, help_text='User Id from the Users model')
    start_time = models.DateTimeField(null=True, blank=True, help_text='Start time of the activity')
    end_time = models.DateTimeField(null=True, blank=True, help_text='End time of the activity')

    # Metadata
    class Meta:
        ordering = ['-start_time', '-end_time']

    # Methods
    def __str__(self):
        return str(self.user_id)

