# Generated by Django 4.0.5 on 2022-07-06 08:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_user_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('time', models.CharField(max_length=100)),
                ('health_issue', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.doctor_profile')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='myapp.user')),
            ],
        ),
    ]
