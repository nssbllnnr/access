from django.db import models

# Create your models here.
class Employees(models.Model):
    DEPARTMENT_CHOISES = (
        ("en", "en"),
        ("kz", "kz"),
        ("ru", "ru"),
    )
    POSITION_CHOISES = (
        ("Teacher", "Teacher"),
        ("Student", "Student"),
    )
    GENDER_CHOISES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    ADVISOR_CHOISES = (
        ("Assem Talasbek", "Assem Talasbek"),
        ("Nazim Ibragim", "Nazim Ibragim"),
    )
    id = models.AutoField(primary_key=True)
    photo = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOISES, default="en", null=True)
    position = models.CharField(max_length=30, choices=POSITION_CHOISES, null=True)
    person_id = models.CharField(max_length=30, blank=True, unique=True, null=False)
    gender = models.CharField(max_length=30, null=True, choices=GENDER_CHOISES)
    email = models.EmailField(max_length=254, null=True)
    advisor = models.CharField(max_length=30, null=True)
    reg_date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name
        
class Access(models.Model):
    card_id = models.CharField(primary_key=True, max_length=30, blank=True, unique=True, null=False)
    access = models.BooleanField(blank=True, default=False, null=False)
    user = models.ForeignKey(Employees, on_delete=models.CASCADE, null=True)
    registred_date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.card_id

class Device(models.Model):
    STATUS = (
        ('IN', 'IN'),
        ('OUT', 'OUT'),
    )
    device_ip = models.CharField(primary_key=True, max_length=30, null=False)
    serial_number = models.CharField(max_length=30, null=True)
    device_model = models.CharField(max_length=30, null=True)
    is_out = models.CharField(max_length=30, null=True, choices=STATUS)
    wait_time = models.IntegerField(default=2)
    check_out = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.device_ip

class History(models.Model):
    STATUS = (
        ('IN', 'IN'),
        ('OUT', 'OUT'),
    )
    entry_date = models.DateTimeField(auto_now_add=True, null=True)
    card = models.ForeignKey(Access, on_delete=models.CASCADE, null=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.entry_date
        
