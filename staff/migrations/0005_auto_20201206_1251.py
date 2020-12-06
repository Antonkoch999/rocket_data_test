# Generated by Django 3.1.4 on 2020-12-06 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0004_auto_20201206_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemptt',
            name='employment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employeemptt',
            name='middle_name',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='employeemptt',
            name='name',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='employeemptt',
            name='role',
            field=models.CharField(blank=True, choices=[('Chief_technical_officer', 'Chief_technical_officer'), ('TeamLead', 'TeamLead'), ('Senior', 'Senior'), ('Middle', 'Middle'), ('Junior', 'Junior')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='employeemptt',
            name='salary',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Salary in $'),
        ),
        migrations.AlterField(
            model_name='employeemptt',
            name='surname',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='employeemptt',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
