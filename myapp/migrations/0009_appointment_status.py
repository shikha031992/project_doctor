# Generated by Django 4.0.5 on 2022-07-08 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_appoinment_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
