from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Student(models.Model):
    """Student model representing individual students"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    roll_no = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(3)])
    name = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)
    subject = models.CharField(max_length=100, blank=True, null=True, help_text="Primary subject/course")
    
    class Meta:
        ordering = ['roll_no']
    
    def __str__(self):
        return f"{self.name} ({self.roll_no})"


class Teacher(models.Model):
    """Teacher model representing individual teachers"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, help_text="Subject taught")
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"


class Attendance(models.Model):
    """Attendance model for recording daily attendance"""
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['student', 'date']
        ordering = ['-date', 'student__roll_no']
    
    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"


class Leave(models.Model):
    """Leave model for student leave requests"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='leave_requests')
    date = models.DateField()
    reason = models.TextField(max_length=500)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    approval = models.CharField(max_length=100, blank=True, help_text="Approval notes")
    approved_by = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_leaves')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"
