# Generated by Django 5.1.4 on 2024-12-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='state',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='zip_code',
            field=models.CharField(max_length=30),
        ),
    ]
