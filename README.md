# 📋 Django To-Do List Application

A full-featured task management web application built with **Django 5.2** and **Python**, designed for efficient personal productivity tracking.

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| **User Authentication** | Secure registration, login, and logout functionality using Django's built-in auth system |
| **Task Management** | Full CRUD operations — Create, Read, Update, and Delete tasks |
| **Task Completion** | Toggle tasks as complete/incomplete with a single click |
| **Task Details** | Dedicated detail view for each task with full information display |
| **Form Validation** | Server-side validation using Django ModelForms |
| **User Feedback** | Flash messages for successful actions (task created, updated, deleted, account created) |
| **Responsive Design** | Clean, user-friendly interface with intuitive navigation |

---

## 🛠️ Tech Stack

- **Backend:** Django 5.2 (Python 3.x)
- **Database:** SQLite3 (default, production-ready)
- **Frontend:** HTML5, CSS, Django Template Engine
- **Authentication:** Django.contrib.auth with custom user registration
- **Forms:** Django ModelForms with built-in validation

---

## 📁 Project Structure

```
To-Do-List/
├── ToDoList/              # Django project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py            # Root URL routing
│   └── wsgi.py            # WSGI application
├── mytodo/                # Main task management app
│   ├── models.py          # Jobs model (task, description, time, is_completed)
│   ├── views.py           # Business logic (CRUD + toggle)
│   ├── forms.py           # Task form with validation
│   ├── urls.py            # App URL routing
│   └── templates/         # HTML templates
├── users/                 # Authentication app
│   ├── views.py           # Register, login, logout views
│   ├── forms.py           # Custom registration form
│   └── templates/         # Auth-related templates
└── db.sqlite3             # SQLite database
```

---

## 🔧 Installation & Setup

```bash
# Clone the repository
git clone <repository-url>
cd To-Do-List

# Activate virtual environment
.venv\Scripts\Activate.ps1    # Windows
# OR
source .venv/bin/activate     # Linux/Mac

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to use the application.

---

## 🎯 Key Technical Skills Demonstrated

- ✅ Django MVC architecture (Models, Views, Templates)
- ✅ Django Forms & ModelForms with validation
- ✅ User authentication & authorization
- ✅ URL routing & namespace
- ✅ Database migrations & models
- ✅ Flash messaging framework
- ✅ HTTP methods handling (GET, POST)
- ✅ Template inheritance & context rendering

---

## 📄 License

MIT License — Feel free to use and modify this project. 
