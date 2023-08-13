from django import forms
from .models import User, Project, Expense

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Project Name", max_length=200)
    description = forms.CharField(label="Description", widget=forms.Textarea)

class CreateNewExpense(forms.Form):
    amount = forms.FloatField(label="Amount")
    date = forms.DateField(label="Expense Date")
    description = forms.CharField(label="Description", widget=forms.Textarea)
    pdf_file = forms.FileField(label="Upload PDF")
    associated_project = forms.ModelChoiceField(queryset=Project.objects.all())
    # Note: You'd typically not let any user select any 'entered_by'. It'd typically be the logged-in user.

class CreateNewUser(forms.Form):
    username = forms.CharField(label="Username", max_length=200)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)
    assigned_project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
