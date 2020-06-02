from django.db.models import Model, CharField, FloatField, ForeignKey, IntegerField, ImageField, AutoField, CASCADE, DateTimeField, BooleanField
from django.contrib.auth.models import User;

# Create your models here

class Employee(Model):
    DEPORTMENT = [("en", "en"),("kz", "kz"), ("ru", "ru")]

    POSITION = [("student", "student"), ("teacher", "teacher")]

    image = ImageField(blank=True, null=True)

    student_id = CharField(max_length=30)
    name = CharField(max_length=30)
    surname = CharField(max_length=30)

    deportment = CharField(max_length=11, choices=DEPORTMENT, default="en")
    position = CharField(max_length=11, choices=POSITION, default="student")

    check_in = DateTimeField(auto_now_add=True)
    check_out = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Name : {self.name}\nSurname : {self.surname}\nStudentId : {self.student_id}\nDeportment : {self.deportment}\nPosition : {self.position}\nCheckIn : {self.check_in}\nCheckOut : {self.check_out}'


class Device(Model):
    STATUS = (
        ('IN', 'IN'),
        ('OUT', 'OUT'),
    )
    device_ip = CharField(primary_key=True, max_length=30, null=False)
    serial_number = CharField(max_length=30, null=True)
    device_model = CharField(max_length=30, null=True)
    is_out = CharField(max_length=30, null=True, choices=STATUS)
    wait_time = IntegerField(default=2)
    last_activity = DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f'SerialNumber : {self.serial_number}\nDeviceIp : {self.device_ip}\nDeviceModel : {self.device_model}\nLastActivity : {self.last_activity}'

class Access(Model):

    card_id = CharField(primary_key=True, max_length=30, blank=True, unique=True, null=False)
    access = BooleanField(blank=True, default=False, null=False)
    user = ForeignKey(Employee, on_delete=CASCADE, null=True)
    registred_date = DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'CardId : {self.card_id}\nAccess : {self.access}\nUser : {self.user}\nRegistredDate : {self.registred_date}'

class History(Model):
    STATUS = (
        ('IN', 'IN'),
        ('OUT', 'OUT'),
    )
    entry_date = DateTimeField(auto_now_add=True, null=True)
    out_date = DateTimeField(null=True)
    card = ForeignKey(Access, on_delete=CASCADE, null=True)
    device = ForeignKey(Device, on_delete=CASCADE, null=True)

    def __str__(self):
        return f'EntryData : {self.entry_date}\nCard : {self.card}\nDevice : {self.device}'