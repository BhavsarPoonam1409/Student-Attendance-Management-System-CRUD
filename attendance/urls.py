from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('add-student/', views.add_student, name='add_student'),
    path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),

    path('add-subject/', views.add_subject, name='add_subject'),

    path('add-attendance/', views.add_attendance, name='add_attendance'),
    path('edit-attendance/<int:id>/', views.edit_attendance, name='edit_attendance'),
    path('delete-attendance/<int:id>/', views.delete_attendance, name='delete_attendance'),
]