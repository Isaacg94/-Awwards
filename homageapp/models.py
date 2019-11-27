from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from tinymce.models import HTMLField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    bio = HTMLField()
    profile_pic = ImageField(manual_crop ='1080x1080')
    contact_info = models.CharField(max_length=144)


class Project(models.Model):
    profile = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=144)
    description = models.TextField()
    img = ImageField()
    live_site = models.CharField(max_length=256)

    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects