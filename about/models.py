from django.db import models

# Create your models here.

class About(models.Model):
    about_title = models.CharField(max_length=30)
    about_description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return f'{self.about_title}'
    
class Socials(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=500)

    class Meta:
        verbose_name_plural = 'Social Media'
    def __str__(self):
        return f'{self.name}'