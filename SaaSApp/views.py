from django.shortcuts import render, redirect
from .models import User, Project, Expense
from .forms import CreateNewExpense, CreateNewUser, CreateNewProject

def index(request):
    title = "SaaSExpenseTracker"
    return render(request, 'index.html', {'title': title})

def about(request):
    return render(request, 'about.html')

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': all_projects})

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {'form': CreateNewProject()})
    else:
        form = CreateNewProject(request.POST)
        if form.is_valid():
            project = Project.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
            )
            return redirect('/projects')
        else:
            return render(request, 'projects/create_project.html', {'form': form})

def expenses(request):
    all_expenses = Expense.objects.all()
    return render(request, 'expenses/expenses.html', {'expenses': all_expenses})

def create_expense(request):
    if request.method == 'GET':
        return render(request, 'expenses/create_expense.html', {'form': CreateNewExpense()})
    else:
        Expense.objects.create(
            amount=request.POST['amount'],
            date=request.POST['date'],
            description=request.POST['description'],
            associated_project_id=request.POST['associated_project'])
        return redirect('/expenses')

def create_user(request):
    if request.method == 'GET':
        return render(request, 'users/create_user.html', {'form': CreateNewUser()})
    else:
        User.objects.create(
            username=request.POST['username'],
            email=request.POST['email'],
            encrypted_password=request.POST['password'],
            role=request.POST['role'])
        return redirect('/users')

def users(request):
    all_users = User.objects.all()
    return render(request, 'users/users.html', {'users': all_users})