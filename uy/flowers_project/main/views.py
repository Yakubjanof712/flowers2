from django.shortcuts import render, redirect
from .forms import CourseForm, LessonForm, TurlarForm, GullarForm
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_course')
    else:
        form = CourseForm()
    return render(request, 'main/add_course.html', {'form': form})
def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_lesson')
    else:
        form = LessonForm()
    return render(request, 'main/add_lesson.html', {'form': form})
def add_turlar(request):
    if request.method == 'POST':
        form = TurlarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_turlar')
    else:
        form = TurlarForm()
    return render(request, 'main/add_turlar.html', {'form': form})
def add_gullar(request):
    if request.method == 'POST':
        form = GullarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_gullar')
    else:
        form = GullarForm()
    return render(request, 'main/add_gullar.html', {'form': form})
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
