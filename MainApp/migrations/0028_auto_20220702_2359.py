# Generated by Django 3.2.10 on 2022-07-02 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0027_auto_20220702_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='adress',
            field=models.CharField(default='Не вказано', max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='facebook',
            field=models.CharField(default='Не вказано', max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='instagram',
            field=models.CharField(default='Не вказано', max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_director',
            field=models.CharField(default='Не вказано', max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_profil',
            field=models.CharField(default='Не вказано', max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_type',
            field=models.CharField(default='Не вказано', max_length=255),
        ),
    ]