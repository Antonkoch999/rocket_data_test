# Generated by Django 3.1.4 on 2020-12-05 07:14

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeMptt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Chief_technical_officer', 'Chief_technical_officer'), ('TeamLead', 'TeamLead'), ('Senior', 'Senior'), ('Middle', 'Middle'), ('Junior', 'Junior')], max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('employment_date', models.DateField()),
                ('salary', models.IntegerField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='staff.employeemptt')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InformationPaidSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('salary', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.employeemptt')),
            ],
        ),
    ]