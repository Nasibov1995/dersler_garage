# Generated by Django 4.2.2 on 2023-06-19 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elan',
            name='muqavile',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='elan',
            name='rejm',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='elan',
            name='staj',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='elan',
            name='tehsil',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='elan',
            name='yash',
            field=models.CharField(max_length=100),
        ),
    ]
