# By Andy Nguyen
from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors["name"] = "Course name is required"
        elif len(postData['name']) <= 5:
            errors["name"] = "Course name must be more than 5 characters"
        if len(postData['desc']) < 1:
            errors["desc"] = "Course description required"
        elif len(postData['desc']) <= 15:
            errors["desc"] = "Course description must be more than 15 characters"
        if Course.objects.filter(name = postData['name']):
            errors["name"] = "Sorry, this course already exists"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Course: {self.id} {self.name} {self.desc}>"
    
    objects = CourseManager()