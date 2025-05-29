from django.db import models
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image

# Create your models here.


class Hero(models.Model):
    title=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=300)
    description=models.CharField(max_length=500)
    image=models.ImageField()


    class Meta:
        verbose_name='Hero'
        verbose_name_plural='Hero'


    def __str__(self):
        return '{0} {1}'.format(self.title,self.subtitle)
    

class About(models.Model):
    title=models.CharField(max_length=50)
    desccription=models.CharField(max_length=250)
    icon=models.CharField(max_length=30)



class Meta:
    verbose_name='About'
    verbose_name_plural='About'


def __str__(self):
    return self.title



class Project(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    link=models.CharField(max_length=250)
    image=models.ImageField()

    # override the save method and
    # use the Image class of the PIL package
    # to convert it to JPEG


    # your_app/models.py
from django.db import models
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
import os

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.CharField(max_length=250, blank=True)

    def save(self, *args, **kwargs):
        if self.image and self.image.name:
            try:
                # Open the uploaded image
                image = Image.open(self.image)
                # Generate a safe filename (replace original extension with .jpg)
                filename = f"{os.path.splitext(self.image.name)[0]}.jpg"
                # Handle PNG images with alpha channel
                if image.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', image.size, (255, 255, 255))  # White background
                    background.paste(image, mask=image.split()[-1])
                    image = background
                # Convert to JPEG and save to BytesIO
                image_io = BytesIO()
                image.save(image_io, format='JPEG', quality=100)
                # Update the image field with the new JPEG
                self.image.save(filename, ContentFile(image_io.getvalue()), save=False)
            except FileNotFoundError as e:
                print(f"FileNotFoundError: {e}")
                # Skip image processing but continue saving the model
                pass
            except Exception as e:
                print(f"Error processing image: {e}")
                # Optionally, raise or handle the error
                pass
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name






            






