# Generated by Django 4.2.4 on 2023-08-12 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SaaSApp', '0002_rename_expenses_expense_rename_projects_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='Missing description'),
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
