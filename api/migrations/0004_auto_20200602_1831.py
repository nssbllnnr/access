# Generated by Django 3.0.6 on 2020-06-02 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200602_1813'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Personal',
        ),
        migrations.AddField(
            model_name='employee',
            name='deportment',
            field=models.CharField(choices=[('en', 'en'), ('kz', 'kz'), ('ru', 'ru')], default='en', max_length=11),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('student', 'student'), ('teacher', 'teacher')], default='student', max_length=11),
        ),
    ]
