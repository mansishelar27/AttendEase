# AttendEase - Project Information & Structure

## 📋 Project Overview

**AttendEase** is a web-based student attendance tracking system built with Django. It enables teachers to digitally record student attendance and allows students to view their attendance records in real-time. The system also includes leave management functionality where students can apply for leave and teachers can approve or reject requests.

---

## 🏗️ Project Structure

```
ATTT/
│
├── ATTT/                          # Main project directory
│   ├── attendance/                # Main Django application
│   │   ├── __init__.py
│   │   ├── admin.py              # Django admin configuration
│   │   ├── apps.py               # App configuration
│   │   ├── forms.py              # Form definitions
│   │   ├── models.py             # Database models
│   │   ├── urls.py               # URL routing
│   │   ├── views.py              # View functions
│   │   └── migrations/           # Database migrations
│   │       ├── __init__.py
│   │       ├── 0001_initial.py
│   │       └── 0002_alter_student_subject.py
│   │
│   ├── attendease/                # Django project settings
│   │   ├── __init__.py
│   │   ├── settings.py           # Project settings
│   │   ├── urls.py               # Root URL configuration
│   │   ├── wsgi.py               # WSGI configuration
│   │   └── asgi.py               # ASGI configuration
│   │
│   ├── templates/                 # HTML templates
│   │   └── attendance/
│   │       ├── base.html         # Base template
│   │       ├── home.html         # Homepage
│   │       ├── login.html        # Login page
│   │       ├── register.html     # Registration page
│   │       ├── student_dashboard.html
│   │       ├── teacher_dashboard.html
│   │       ├── mark_attendance.html
│   │       ├── view_attendance.html
│   │       ├── apply_leave.html
│   │       ├── leave_requests.html
│   │       └── approve_leave.html
│   │
│   ├── static/                    # Static files
│   │   └── css/
│   │       └── style.css         # Custom CSS styles
│   │
│   ├── db.sqlite3                 # SQLite database
│   ├── manage.py                  # Django management script
│   ├── requirements.txt           # Python dependencies
│   ├── README.md                  # Project documentation
│   └── PROJECT_INFO.md            # This file
│
└── my_venv/                       # Virtual environment (not in repo)
    ├── Scripts/                   # Windows activation scripts
    ├── Lib/                       # Python packages
    └── Include/                   # Header files
```

---

## 🗄️ Database Models

### 1. **Student Model**
- **Fields:**
  - `user` (OneToOneField to User)
  - `roll_no` (CharField, unique, min 3 chars)
  - `name` (CharField, max 100)
  - `date_joined` (DateField, auto)
  - `subject` (CharField, optional - nullable)
- **Relationships:** One-to-one with User, one-to-many with Attendance and Leave

### 2. **Teacher Model**
- **Fields:**
  - `user` (OneToOneField to User)
  - `name` (CharField, max 100)
  - `subject` (CharField, max 100)
- **Relationships:** One-to-one with User, one-to-many with Attendance and Leave approvals

### 3. **Attendance Model**
- **Fields:**
  - `student` (ForeignKey to Student)
  - `teacher` (ForeignKey to Teacher)
  - `date` (DateField)
  - `status` (CharField: 'present' or 'absent')
  - `created_at` (DateTimeField, auto)
  - `updated_at` (DateTimeField, auto)
- **Constraints:** Unique together (student, date)

### 4. **Leave Model**
- **Fields:**
  - `student` (ForeignKey to Student)
  - `date` (DateField)
  - `reason` (TextField, max 500)
  - `status` (CharField: 'pending', 'approved', 'rejected')
  - `approval` (CharField, optional)
  - `approved_by` (ForeignKey to Teacher, optional)
  - `created_at` (DateTimeField, auto)
  - `updated_at` (DateTimeField, auto)

---

## 🔗 URL Routes

### Public Routes
- `/` - Home page
- `/login/` - User login
- `/register/student/` - Student registration
- `/register/teacher/` - Teacher registration

### Student Routes (Requires Login)
- `/dashboard/` - Redirects to student/teacher dashboard
- `/student/dashboard/` - Student dashboard
- `/view-attendance/` - View attendance records
- `/apply-leave/` - Apply for leave

### Teacher Routes (Requires Login)
- `/teacher/dashboard/` - Teacher dashboard with attendance summary
- `/mark-attendance/` - Mark attendance for students
- `/leave-requests/` - View all leave requests
- `/approve-leave/<id>/` - Approve/reject leave request

### Admin
- `/admin/` - Django admin panel

---

## 📦 Dependencies

### Core Dependencies
- **Django 4.2.7** - Web framework
- **Pillow 10.1.0** - Image processing (if needed)
- **python-decouple 3.8** - Environment variable management

### Frontend Libraries (CDN)
- **Bootstrap 5.3.0** - CSS framework
- **Font Awesome 6.0.0** - Icons
- **Chart.js** - Data visualization (for attendance charts)

---

## 🎯 Key Features

### Student Features
1. **Registration & Authentication**
   - Student registration with roll number
   - Secure login/logout
   - No subject/course field required

2. **Dashboard**
   - Attendance percentage display
   - Recent attendance records
   - Quick actions (View Attendance, Apply Leave)

3. **Attendance Viewing**
   - Complete attendance history
   - Statistics (total, present, absent, percentage)
   - Filterable records
   - Visual charts and progress bars

4. **Leave Management**
   - Apply for leave with date and reason
   - View leave request status
   - No leave guidelines section
   - No recent leave requests display

### Teacher Features
1. **Registration & Authentication**
   - Teacher registration with subject
   - Secure login/logout

2. **Dashboard**
   - Total students count
   - Subject display
   - Attendance summary with filters (Day/Week/Month/Year)
   - Student attendance history by subject

3. **Attendance Marking**
   - Date selection
   - Mark present/absent for each student
   - Date column displayed in table
   - Save attendance records

4. **Leave Management**
   - View all leave requests
   - Approve/reject leave requests
   - No approval notes field
   - No quick actions section

---

## 🎨 UI/UX Features

- **Responsive Design:** Works on desktop, tablet, and mobile
- **Modern Bootstrap 5:** Clean, professional interface
- **Color-coded Status:**
  - Green: Present/Approved/Good attendance
  - Red: Absent/Rejected/Low attendance
  - Yellow: Pending/Average attendance
- **Interactive Elements:** Hover effects, smooth transitions
- **Data Visualization:** Progress bars, charts, statistics cards
- **Font Awesome Icons:** Visual indicators throughout

---

## 🔐 Security Features

- **Django Authentication:** Built-in user authentication
- **CSRF Protection:** Enabled for all forms
- **Role-based Access:** Different views for students and teachers
- **Login Required Decorators:** Protected routes
- **Password Validation:** Django's password validators
- **Secure Sessions:** Django session management

---

## 🗂️ File Organization

### Backend Files
- **models.py:** Database schema definitions
- **views.py:** Business logic and request handling
- **forms.py:** Form definitions and validation
- **urls.py:** URL routing configuration
- **admin.py:** Django admin customization

### Frontend Files
- **Templates:** HTML files with Django template syntax
- **Static CSS:** Custom styling in `style.css`
- **Base Template:** Common layout in `base.html`

---

## 🚀 Running the Project

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Setup Steps
1. Activate virtual environment:
   ```bash
   my_venv\Scripts\activate  # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

5. Run development server:
   ```bash
   python manage.py runserver
   ```

6. Access application:
   - Home: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

---

## 📊 Database Schema Summary

```
User (Django built-in)
  ├── Student (OneToOne)
  │   ├── Attendance (ManyToOne)
  │   └── Leave (ManyToOne)
  │
  └── Teacher (OneToOne)
      ├── Attendance (ManyToOne)
      └── Leave Approvals (ManyToOne)
```

---

## 🔄 Recent Changes Made

1. **Removed subject field from student registration**
   - Subject field made optional in Student model
   - Removed from registration form and templates

2. **Updated teacher dashboard**
   - Removed "Today's Attendance" and "Pending Leaves" sections
   - Added "Attendance Summary" with Day/Week/Month/Year filters
   - Removed "Total Days" and "Status" columns from summary table
   - Removed "Total Records" statistics card

3. **Updated attendance marking**
   - Added date column next to status column
   - Date displays dynamically based on selected date

4. **Updated leave management**
   - Removed "Leave Guidelines" from apply leave page
   - Removed "Recent Leave Requests" section
   - Removed "Approval Notes" field from approve leave page
   - Removed "Quick Actions" section from approve leave page

5. **Home page updates**
   - Removed "Why Choose AttendEase?" section
   - Updated copyright year to 2025

---

## 📝 Notes

- **Database:** SQLite for development (can be switched to PostgreSQL for production)
- **Static Files:** Served from `static/` directory
- **Templates:** Located in `templates/attendance/`
- **Virtual Environment:** Located in `my_venv/` (not tracked in version control)
- **Migrations:** Two migrations applied (initial and subject field alteration)

---

## 🎓 Project Purpose

This project is designed for educational institutions to:
- Replace paper-based attendance systems
- Provide real-time attendance tracking
- Enable digital leave management
- Offer transparency to students about their attendance
- Simplify administrative tasks for teachers

---

**Last Updated:** 2025
**Django Version:** 4.2.7
**Python Version:** 3.8+

