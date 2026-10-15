from django import forms
from .models import Student, Subject, Attendance


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'enrollment_no', 'course', 'semester']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name']


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'subject', 'date', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }