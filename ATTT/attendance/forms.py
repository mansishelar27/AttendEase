from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Teacher, Attendance, Leave


class StudentRegistrationForm(UserCreationForm):
    """Form for student registration"""
    email = forms.EmailField(required=True)
    roll_no = forms.CharField(max_length=20, required=True, help_text="Enter your roll number")
    name = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'roll_no', 'name')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Student.objects.create(
                user=user,
                roll_no=self.cleaned_data['roll_no'],
                name=self.cleaned_data['name']
            )
        return user


class TeacherRegistrationForm(UserCreationForm):
    """Form for teacher registration"""
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=100, required=True)
    subject = forms.CharField(max_length=100, required=True, help_text="Subject you teach")
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'name', 'subject')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Teacher.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                subject=self.cleaned_data['subject']
            )
        return user


class AttendanceForm(forms.ModelForm):
    """Form for marking attendance"""
    class Meta:
        model = Attendance
        fields = ['student', 'status']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class LeaveRequestForm(forms.ModelForm):
    """Form for student leave requests"""
    class Meta:
        model = Leave
        fields = ['date', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Enter reason for leave...'}),
        }


class LeaveApprovalForm(forms.ModelForm):
    """Form for teacher to approve/reject leave requests"""
    class Meta:
        model = Leave
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
