from django.contrib import admin
from .models import Course, Lesson, Turlar, Gullar

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration']
    search_fields = ['name']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    search_fields = ['title']

@admin.register(Turlar)
class TurlarAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Gullar)
class GullarAdmin(admin.ModelAdmin):
    list_display = ['name', 'turlar']
    search_fields = ['name']
    list_filter = ['turlar']
    readonly_fields = ['image_preview']
    fields = ['turlar', 'name', 'image', 'image_preview']

    def image_preview(self, obj):
        from django.utils.html import mark_safe
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "-"
    image_preview.short_description = "Image Preview"
