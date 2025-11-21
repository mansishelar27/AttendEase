from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, Teacher, Attendance, Leave


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'name', 'subject', 'date_joined']
    list_filter = ['subject', 'date_joined']
    search_fields = ['roll_no', 'name', 'user__email']
    readonly_fields = ['date_joined']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'user']
    list_filter = ['subject']
    search_fields = ['name', 'user__email']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'teacher', 'date', 'status']
    list_filter = ['status', 'date', 'teacher']
    search_fields = ['student__name', 'student__roll_no']
    date_hierarchy = 'date'


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'status', 'approved_by', 'created_at']
    list_filter = ['status', 'date', 'created_at']
    search_fields = ['student__name', 'student__roll_no', 'reason']
    readonly_fields = ['created_at', 'updated_at']
