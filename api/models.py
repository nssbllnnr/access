from django.db.models import Model, CharField, FloatField, ForeignKey, IntegerField, ImageField, AutoField, CASCADE, DateTimeField
from django.contrib.auth.models import User;

# Create your models here

class Employee(Model):

    image = ImageField(blank=True, null=True)

    student_id = CharField(max_length=30)
    name = CharField(max_length=30)
    surname = CharField(max_length=30)

    check_in = DateTimeField(auto_now_add=True)
    check_out = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Name : {self.name}\nSurname : {self.surname}\nStudentId : {self.student_id}\nCheckIn : {self.check_in}\nCheckOut : {self.check_out}'


class Personal(Model):
    DEPORTMENT = [("en", "en"),("kz", "kz"), ("ru", "ru")]

    POSITION = [("student", "student"), ("teacher", "teacher")]

    student_id = CharField(max_length=30)
    name = CharField(max_length=30)
    surname = CharField(max_length=30)

    deportment = CharField(max_length=11, choices=DEPORTMENT, default="en")
    position = CharField(max_length=11, choices=POSITION, default="student")

    last_check = DateTimeField(auto_now_add=True)
    check_out = DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'Name : {self.name}\nSurname : {self.surname}\nStudentId : {self.student_id}\nDeportment : {self.deportment}\nPosition : {self.position}\nLastCheck : {self.last_check}\nCheckOut : {self.check_out}'


class Device(Model):

    serial_number = CharField(max_length=30)
    device_ip = CharField(max_length=30)
    device_model = CharField(max_length=30)
    last_activity = DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f'SerialNumber : {self.serial_number}\nDeviceIp : {self.device_ip}\nDeviceModel : {self.device_model}\nLastActivity : {self.last_activity}'