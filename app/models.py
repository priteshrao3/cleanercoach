from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class ServicePage(models.Model):
    Service_Title =models.CharField(max_length=50)
    First_Service_Image = models.ImageField(upload_to="servimg" )
    First_Service_Content = models.TextField( max_length=2000)
    Service_Subtitle = models.CharField(max_length=200)
    Service_Image_Second = models.ImageField(upload_to="servimg" )
    Service_Image_Third = models.ImageField(upload_to="servimg")
    Second_Service_Content = models.TextField( max_length=2000)

    def title_to_url(self):
        return self.Service_Title.replace(' ', '-')
    

class Project(models.Model):
    image = models.ImageField(upload_to="projectimg" )
    Project_name = models.CharField( max_length=100)
    Project_content = models.CharField(max_length=50)



class Testomonial(models.Model):
    image = models.ImageField(upload_to="testmoimg" )
    clint_coments = models.TextField( max_length=1000)
    name = models.CharField( max_length=100)
    city = models.TextField( max_length=100)


class GalleryImg(models.Model):
    image = models.ImageField(upload_to="gling" )
    Service_Name = models.CharField(max_length=100)



class Video(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    video = EmbedVideoField()

    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-added']
