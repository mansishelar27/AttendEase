from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from datetime import date, datetime, timedelta
from .models import Student, Teacher, Attendance, Leave
from .forms import StudentRegistrationForm, TeacherRegistrationForm, LeaveRequestForm, LeaveApprovalForm


def home(request):
    """Home page view"""
    return render(request, 'attendance/home.html')


def student_register(request):
    """Student registration view"""
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to AttendEase.')
            return redirect('dashboard')
    else:
        form = StudentRegistrationForm()
    return render(request, 'attendance/register.html', {'form': form, 'user_type': 'Student'})


def teacher_register(request):
    """Teacher registration view"""
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to AttendEase.')
            return redirect('dashboard')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'attendance/register.html', {'form': form, 'user_type': 'Teacher'})


@login_required
def dashboard(request):
    """Dashboard view - redirects based on user type"""
    try:
        if hasattr(request.user, 'student_profile'):
            return redirect('student_dashboard')
        elif hasattr(request.user, 'teacher_profile'):
            return redirect('teacher_dashboard')
    except:
        pass
    
    messages.error(request, 'User profile not found. Please contact administrator.')
    return redirect('home')


@login_required
def student_dashboard(request):
    """Student dashboard view"""
    try:
        student = request.user.student_profile
    except:
        messages.error(request, 'Student profile not found.')
        return redirect('home')
    
    # Get attendance records
    attendance_records = Attendance.objects.filter(student=student).order_by('-date')[:10]
    
    # Get leave requests
    leave_requests = Leave.objects.filter(student=student).order_by('-created_at')[:5]
    
    # Calculate attendance percentage
    total_records = Attendance.objects.filter(student=student).count()
    present_records = Attendance.objects.filter(student=student, status='present').count()
    attendance_percentage = (present_records / total_records * 100) if total_records > 0 else 0
    
    context = {
        'student': student,
        'attendance_records': attendance_records,
        'leave_requests': leave_requests,
        'attendance_percentage': round(attendance_percentage, 1),
        'total_records': total_records,
    }
    return render(request, 'attendance/student_dashboard.html', context)


@login_required
def teacher_dashboard(request):
    """Teacher dashboard view"""
    try:
        teacher = request.user.teacher_profile
    except:
        messages.error(request, 'Teacher profile not found.')
        return redirect('home')
    
    # Get all students
    students = Student.objects.all().order_by('roll_no')
    
    # Get filter type from request (day, week, month, year)
    filter_type = request.GET.get('filter', 'week')
    
    # Calculate date range based on filter
    today = date.today()
    start_date = None
    end_date = today
    filter_display = ""
    
    if filter_type == 'day':
        # Get today's date only
        start_date = today
        end_date = today
        filter_display = f"Today ({today.strftime('%b %d, %Y')})"
    elif filter_type == 'week':
        # Get start of current week (Monday)
        days_since_monday = today.weekday()
        start_date = today - timedelta(days=days_since_monday)
        filter_display = f"This Week ({start_date.strftime('%b %d')} - {end_date.strftime('%b %d, %Y')})"
    elif filter_type == 'month':
        # Get start of current month
        start_date = today.replace(day=1)
        filter_display = f"This Month ({start_date.strftime('%B %Y')})"
    elif filter_type == 'year':
        # Get start of current year
        start_date = today.replace(month=1, day=1)
        filter_display = f"This Year ({start_date.strftime('%Y')})"
    
    # Get attendance records for the teacher within the date range
    attendance_records = Attendance.objects.filter(teacher=teacher)
    if start_date:
        attendance_records = attendance_records.filter(date__gte=start_date, date__lte=end_date)
    
    # Calculate attendance summary for each student
    attendance_summary = []
    total_present = 0
    total_absent = 0
    total_records = attendance_records.count()
    
    for student in students:
        student_records = attendance_records.filter(student=student)
        total_days = student_records.count()
        present = student_records.filter(status='present').count()
        absent = student_records.filter(status='absent').count()
        percentage = (present / total_days * 100) if total_days > 0 else 0
        
        total_present += present
        total_absent += absent
        
        attendance_summary.append({
            'roll_no': student.roll_no,
            'name': student.name,
            'total_days': total_days,
            'present': present,
            'absent': absent,
            'percentage': round(percentage, 1),
        })
    
    # Calculate average attendance percentage
    total_avg = 0
    if attendance_summary:
        total_avg = sum(s['percentage'] for s in attendance_summary) / len(attendance_summary)
    
    context = {
        'teacher': teacher,
        'students': students,
        'filter_type': filter_type,
        'filter_display': filter_display,
        'attendance_summary': attendance_summary,
        'total_avg': round(total_avg, 1),
        'total_records': total_records,
    }
    return render(request, 'attendance/teacher_dashboard.html', context)


@login_required
def mark_attendance(request):
    """Mark attendance view for teachers"""
    try:
        teacher = request.user.teacher_profile
    except:
        messages.error(request, 'Teacher profile not found.')
        return redirect('home')
    
    if request.method == 'POST':
        date_str = request.POST.get('date')
        if not date_str:
            messages.error(request, 'Please select a date.')
            return redirect('mark_attendance')
        
        attendance_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        # Mark attendance for each student
        for student in Student.objects.all():
            status = request.POST.get(f'student_{student.id}')
            if status in ['present', 'absent']:
                attendance, created = Attendance.objects.get_or_create(
                    student=student,
                    date=attendance_date,
                    defaults={'teacher': teacher, 'status': status}
                )
                if not created:
                    attendance.status = status
                    attendance.teacher = teacher
                    attendance.save()
        
        messages.success(request, f'Attendance marked successfully for {attendance_date}.')
        return redirect('teacher_dashboard')
    
    students = Student.objects.all().order_by('roll_no')
    return render(request, 'attendance/mark_attendance.html', {'students': students})


@login_required
def view_attendance(request):
    """View attendance records for students"""
    try:
        student = request.user.student_profile
    except:
        messages.error(request, 'Student profile not found.')
        return redirect('home')
    
    # Get all attendance records
    attendance_records = Attendance.objects.filter(student=student).order_by('-date')
    
    # Calculate statistics
    total_records = attendance_records.count()
    present_records = attendance_records.filter(status='present').count()
    absent_records = attendance_records.filter(status='absent').count()
    attendance_percentage = (present_records / total_records * 100) if total_records > 0 else 0
    
    context = {
        'student': student,
        'attendance_records': attendance_records,
        'total_records': total_records,
        'present_records': present_records,
        'absent_records': absent_records,
        'attendance_percentage': round(attendance_percentage, 1),
    }
    return render(request, 'attendance/view_attendance.html', context)


@login_required
def apply_leave(request):
    """Apply for leave view for students"""
    try:
        student = request.user.student_profile
    except:
        messages.error(request, 'Student profile not found.')
        return redirect('home')
    
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.student = student
            leave.save()
            messages.success(request, 'Leave request submitted successfully.')
            return redirect('student_dashboard')
    else:
        form = LeaveRequestForm()
    
    return render(request, 'attendance/apply_leave.html', {'form': form, 'student': student})


@login_required
def leave_requests(request):
    """View and manage leave requests for teachers"""
    try:
        teacher = request.user.teacher_profile
    except:
        messages.error(request, 'Teacher profile not found.')
        return redirect('home')
    
    # Get all leave requests
    leave_requests = Leave.objects.all().order_by('-created_at')
    
    return render(request, 'attendance/leave_requests.html', {
        'leave_requests': leave_requests,
        'teacher': teacher
    })


@login_required
def leave_info(request):
    """Detailed leave information for students"""
    try:
        student = request.user.student_profile
    except:
        messages.error(request, 'Student profile not found.')
        return redirect('home')
    
    leaves = Leave.objects.filter(student=student).order_by('-date')
    leaves_pending = leaves.filter(status='pending')
    leaves_approved = leaves.filter(status='approved')
    leaves_rejected = leaves.filter(status='rejected')
    
    context = {
        'student': student,
        'total_leaves': leaves.count(),
        'pending_count': leaves_pending.count(),
        'approved_count': leaves_approved.count(),
        'rejected_count': leaves_rejected.count(),
        'leaves_pending': leaves_pending,
        'leaves_approved': leaves_approved,
        'leaves_rejected': leaves_rejected,
    }
    return render(request, 'attendance/leave_info.html', context)


@login_required
def approve_leave(request, leave_id):
    """Approve or reject leave request"""
    try:
        teacher = request.user.teacher_profile
    except:
        messages.error(request, 'Teacher profile not found.')
        return redirect('home')
    
    leave = get_object_or_404(Leave, id=leave_id)
    
    if request.method == 'POST':
        form = LeaveApprovalForm(request.POST, instance=leave)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.approved_by = teacher
            leave.save()
            messages.success(request, f'Leave request {leave.status} successfully.')
            return redirect('leave_requests')
    else:
        form = LeaveApprovalForm(instance=leave)
    
    return render(request, 'attendance/approve_leave.html', {
        'form': form,
        'leave': leave,
        'teacher': teacher
    })


def logout_view(request):
    """Logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')
