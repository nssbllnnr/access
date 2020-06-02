# Generated by Django 3.0.6 on 2020-06-02 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=30)),
                ('device_ip', models.CharField(max_length=30)),
                ('device_model', models.CharField(max_length=30)),
                ('last_activity', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
