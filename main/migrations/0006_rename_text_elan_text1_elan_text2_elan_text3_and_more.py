# Generated by Django 4.2.2 on 2023-06-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_elan_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elan',
            old_name='text',
            new_name='text1',
        ),
        migrations.AddField(
            model_name='elan',
            name='text2',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='elan',
            name='text3',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='elan',
            name='text4',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='elan',
            name='text5',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
