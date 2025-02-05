from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    title= models.CharField(max_length=255)
    description= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(User,  on_delete=models.SET_NULL, null =True)

    def __str__(self):
        return self.title
    

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    content = models.TextField()

    def __str__(self):
        return self.title
    

