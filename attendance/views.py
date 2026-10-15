from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Q
from .models import Student, Subject, Attendance
from .forms import StudentForm, SubjectForm, AttendanceForm


def home(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    attendance_records = Attendance.objects.select_related(
        'student', 'subject'
    ).all().order_by('-date')

    student_data = []

    for student in students:
        total = Attendance.objects.filter(student=student).count()

        present = Attendance.objects.filter(
            student=student,
            status='Present'
        ).count()

        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0

        student_data.append({
            'student': student,
            'total': total,
            'present': present,
            'percentage': round(percentage, 2),
        })

    return render(request, 'attendance/home.html', {
        'student_data': student_data,
        'subjects': subjects,
        'attendance_records': attendance_records,
    })


def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'attendance/form.html', {
        'form': form,
        'title': 'Add Student',
    })


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'attendance/form.html', {
        'form': form,
        'title': 'Edit Student',
    })


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('home')

    return render(request, 'attendance/confirm_delete.html', {
        'object': student,
        'title': 'Delete Student',
    })


def add_subject(request):
    form = SubjectForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'attendance/form.html', {
        'form': form,
        'title': 'Add Subject',
    })


def add_attendance(request):
    form = AttendanceForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'attendance/form.html', {
        'form': form,
        'title': 'Mark Attendance',
    })


def edit_attendance(request, id):
    record = get_object_or_404(Attendance, id=id)
    form = AttendanceForm(request.POST or None, instance=record)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'attendance/form.html', {
        'form': form,
        'title': 'Edit Attendance',
    })


def delete_attendance(request, id):
    record = get_object_or_404(Attendance, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('home')

    return render(request, 'attendance/confirm_delete.html', {
        'object': record,
        'title': 'Delete Attendance',
    })