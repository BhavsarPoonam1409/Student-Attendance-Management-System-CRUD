from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment_no = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    semester = models.IntegerField()

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class Attendance(models.Model):

    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    def __str__(self):
        return self.student.name + " - " + self.status