from django.contrib import admin
from .models import User, Project, Expense

# Register your models here.
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Expense)
