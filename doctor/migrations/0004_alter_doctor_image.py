# Generated by Django 4.2.6 on 2024-01-25 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_rename_name_doctor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(upload_to='doctor/images/'),
        ),
    ]