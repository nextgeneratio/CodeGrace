from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import TeamMember, Project, Task


def home(request):
    projects = Project.objects.filter(is_active=True)
    members = TeamMember.objects.select_related('user').all()
    return render(request, 'core/home.html', {'projects': projects, 'members': members})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            TeamMember.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Account created! Welcome to CodeGrace.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})


@login_required
def project_list(request):
    projects = Project.objects.filter(is_active=True)
    return render(request, 'core/project_list.html', {'projects': projects})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = project.tasks.select_related('assigned_to').all()
    return render(request, 'core/project_detail.html', {'project': project, 'tasks': tasks})


@login_required
def team_view(request):
    members = TeamMember.objects.select_related('user').all()
    return render(request, 'core/team.html', {'members': members})
