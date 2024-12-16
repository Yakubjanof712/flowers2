from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in hours")

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=255)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Turlar(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Gullar(models.Model):
    turlar = models.ForeignKey(Turlar, on_delete=models.CASCADE, related_name="gullar")
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="gullar_images/")

    def __str__(self):
        return self.name
