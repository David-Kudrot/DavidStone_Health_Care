# Generated by Django 4.2.6 on 2024-01-24 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='user',
            new_name='name',
        ),
    ]
