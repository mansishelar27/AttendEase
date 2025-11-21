# AttendEase - Web-Based Student Attendance Tracker

AttendEase is a modern, web-based student attendance tracking system that enables teachers to record student attendance efficiently and allows students to view their attendance records. This system replaces traditional paper registers with a simple, accessible digital solution.

## 🚀 Features

### For Students
- **Student Registration & Login**: Secure authentication system
- **View Attendance Records**: Real-time access to attendance history with detailed statistics
- **Apply for Leave**: Submit leave requests with detailed reasons
- **Dashboard**: Overview of attendance percentage and recent records
- **Responsive Design**: Access from any device, anywhere

### For Teachers
- **Teacher Registration & Login**: Secure authentication system
- **Mark Attendance**: Digital attendance recording with date selection
- **Review Leave Requests**: Approve or reject student leave applications
- **Student Management**: View all students and their attendance records
- **Dashboard**: Overview of pending tasks and daily statistics

### System Features
- **Role-based Access Control**: Different interfaces for students and teachers
- **Secure Database Storage**: All records stored in SQLite database
- **Modern UI/UX**: Bootstrap-based responsive design
- **Real-time Updates**: Instant updates across the system
- **Data Visualization**: Charts and statistics for better insights

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Backend**: Python 3.x with Django Framework
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Icons**: Font Awesome 6
- **Charts**: Chart.js

## 📋 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for version control)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ATTT
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📱 Usage

### For Students

1. **Registration**: Visit the homepage and click "Register as Student"
2. **Login**: Use your credentials to access the student dashboard
3. **View Attendance**: Check your attendance records and statistics
4. **Apply Leave**: Submit leave requests with detailed reasons

### For Teachers

1. **Registration**: Visit the homepage and click "Register as Teacher"
2. **Login**: Use your credentials to access the teacher dashboard
3. **Mark Attendance**: Select date and mark attendance for all students
4. **Review Leaves**: Approve or reject student leave requests

## 🗄️ Database Schema

The system uses the following main models:

- **Student**: Student information and profile
- **Teacher**: Teacher information and profile
- **Attendance**: Daily attendance records
- **Leave**: Student leave requests and approvals
- **User**: Django's built-in user authentication

## 📁 Project Structure

```
ATTT/
├── attendease/              # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── attendance/              # Main application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/               # HTML templates
│   └── attendance/
│       ├── base.html
│       ├── home.html
│       ├── login.html
│       ├── register.html
│       ├── student_dashboard.html
│       ├── teacher_dashboard.html
│       ├── mark_attendance.html
│       ├── view_attendance.html
│       ├── apply_leave.html
│       ├── leave_requests.html
│       └── approve_leave.html
├── static/                  # Static files
│   └── css/
│       └── style.css
├── manage.py
├── requirements.txt
└── README.md
```

## 🎨 UI/UX Features

- **Modern Design**: Clean, professional interface using Bootstrap 5
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile
- **Interactive Elements**: Hover effects, animations, and smooth transitions
- **Color-coded Status**: Visual indicators for attendance and leave status
- **Data Visualization**: Charts and progress bars for better insights
- **Accessibility**: Proper contrast ratios and keyboard navigation

## 🔒 Security Features

- **User Authentication**: Secure login/logout system
- **Role-based Access**: Different permissions for students and teachers
- **CSRF Protection**: Built-in Django CSRF protection
- **Input Validation**: Form validation and sanitization
- **Secure Sessions**: Django's secure session management

## 🚀 Deployment

### For Production Deployment:

1. **Environment Variables**: Set up environment variables for sensitive data
2. **Database**: Switch to PostgreSQL or MySQL for production
3. **Static Files**: Configure static file serving
4. **Security**: Update Django settings for production
5. **Web Server**: Use Gunicorn with Nginx

### Example Production Settings:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'attendease_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the documentation
2. Search existing issues
3. Create a new issue with detailed description
4. Contact the development team

## 🎯 Future Enhancements

- [ ] Email notifications for leave approvals
- [ ] Bulk attendance marking
- [ ] Attendance reports and analytics
- [ ] Mobile app development
- [ ] Integration with school management systems
- [ ] Advanced user roles and permissions
- [ ] Data export functionality
- [ ] Automated attendance reminders

## 📊 System Requirements

- **Minimum Python Version**: 3.8
- **RAM**: 512MB minimum, 1GB recommended
- **Storage**: 100MB for application, additional space for database
- **Browser Support**: Chrome, Firefox, Safari, Edge (latest versions)

---

**AttendEase** - Simplifying attendance management for educational institutions.

Made with ❤️ using Django and Bootstrap.
