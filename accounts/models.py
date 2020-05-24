from django.db import models

# Create your models here.
class Employees(models.Model):
    STATUS = (
        ('Teacher','Teacher'),
        ('Student','Student'),
    )
    name = models.CharField(max_length=30,null=True)
    surname = models.CharField(max_length=30,null=True)
    status = models.CharField(max_length=30,null=True,choices=STATUS)
    student_id = models.CharField(max_length=30,blank=True,unique=True,null=False)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name

class Members(models.Model):
    name = models.CharField(max_length=30,null=True)
    surname = models.CharField(max_length=30,null=True)
    student_id = models.CharField(max_length=30,blank=True,unique=True,null=False)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    date_in = models.DateTimeField(auto_now_add=True,null=True)
    date_out = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name 