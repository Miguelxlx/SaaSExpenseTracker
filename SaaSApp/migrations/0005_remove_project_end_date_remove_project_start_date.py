# Generated by Django 4.2.4 on 2023-08-12 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SaaSApp', '0004_remove_expense_entered_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
    ]
