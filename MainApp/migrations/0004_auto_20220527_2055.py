# Generated by Django 3.2.10 on 2022-05-27 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_alter_school_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='email',
        ),
        migrations.RemoveField(
            model_name='school',
            name='type_school',
        ),
    ]
