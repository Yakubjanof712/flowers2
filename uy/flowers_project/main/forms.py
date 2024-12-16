from django import forms
from .models import Course, Lesson, Turlar, Gullar
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'duration']
class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content', 'video_url']

class TurlarForm(forms.ModelForm):
    class Meta:
        model = Turlar
        fields = ['name', 'description']

class GullarForm(forms.ModelForm):
    class Meta:
        model = Gullar
        fields = ['turlar', 'name', 'image']
