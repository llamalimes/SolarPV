from django.db import models
from django.contrib.auth.models import User
from solarpv.models import Client
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # if user is delete then the profile will be too, but if profile is deleted, it will not delete the user.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    prefix = models.CharField(max_length=10)
    job_title = models.CharField(max_length=100)
    office_phone = models.CharField(max_length=15)
    cell_phone = models.CharField(max_length=15)
    company = models.CharField(max_length=100)
    client_id = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path) # resizes image

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

