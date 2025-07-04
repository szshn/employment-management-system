# Generated by Django 5.2.3 on 2025-06-30 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0003_alter_attendance_employee_alter_performance_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date(2025, 6, 30), verbose_name='Attendance record date'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='review_date',
            field=models.DateField(default=datetime.date(2025, 6, 30), verbose_name='Performance review date'),
        ),
    ]
