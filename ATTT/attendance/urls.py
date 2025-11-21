from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home and authentication
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='attendance/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/student/', views.student_register, name='student_register'),
    path('register/teacher/', views.teacher_register, name='teacher_register'),
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    
    # Attendance
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('view-attendance/', views.view_attendance, name='view_attendance'),
    
    # Leave management
    path('apply-leave/', views.apply_leave, name='apply_leave'),
    path('leave-requests/', views.leave_requests, name='leave_requests'),
    path('leave-info/', views.leave_info, name='leave_info'),
    path('approve-leave/<int:leave_id>/', views.approve_leave, name='approve_leave'),
]
