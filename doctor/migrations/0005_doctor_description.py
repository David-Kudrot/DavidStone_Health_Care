# Generated by Django 4.2.6 on 2024-01-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_alter_doctor_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
