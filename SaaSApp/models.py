from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='Missing description')

    def __str__(self):
        return self.name

class User(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    encrypted_password = models.CharField(max_length=500)  # Typically you'll want to use Django's in-built User model for better security.
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('registrar', 'Registrar'),
        ('account_manager', 'Account Manager')
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    assigned_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Add any other necessary fields like first_name, last_name etc.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    description = models.TextField()
    pdf_file = models.FileField(upload_to='expenses_pdfs/')  # Make sure to have a MEDIA_ROOT and MEDIA_URL configured in settings.
    associated_project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"${self.amount} - {self.description}"
