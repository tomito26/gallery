from django.db import models
from cloudinary.models import CloudinaryField

# Create your models her
class Photo(models.Model):
    image = CloudinaryField('image')
    
  