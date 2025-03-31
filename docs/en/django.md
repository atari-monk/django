# Django

# Introduction

Question_1: Some company is working with Django. I need to know everything about it to prepare for job. Can you teach me?

Content_1: Yes! Django is a powerful web framework for building web applications using Python. I'll break it down step by step to help you master it for your job preparation.  

---

## **1. Introduction to Django**  
Django is a **high-level Python web framework** that encourages **rapid development** and **clean, pragmatic design**. It follows the **MVC (Model-View-Controller)** pattern (although in Django, it’s called **MTV – Model-Template-View**).  

### **Why Django?**  
✅ **Fast Development** – Built-in features like authentication, ORM, admin panel, etc.  
✅ **Security** – Protection against SQL injection, CSRF, XSS, etc.  
✅ **Scalability** – Can handle large applications with proper optimization.  
✅ **Batteries Included** – Many built-in functionalities like forms, user authentication, and session management.  

---

## **2. Setting Up Django**  
### **Installation**  
Make sure you have Python installed (preferably 3.8+). Then install Django using:  
```bash
pip install django
```
To verify the installation:  
```bash
django-admin --version
```

---

## **3. Creating a Django Project**  
Create a new Django project:  
```bash
django-admin startproject myproject
cd myproject
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** in your browser. You should see Django’s default welcome page.  

### **Django Project Structure**  
```
myproject/
│── manage.py        # Command-line utility for Django
│── myproject/       # Project settings
│   │── settings.py  # Project settings (database, middleware, installed apps)
│   │── urls.py      # URL routing
│   │── wsgi.py      # Entry point for WSGI servers
│   │── asgi.py      # Entry point for ASGI servers
│── app/             # Each Django app (to be created)
```

---

## **4. Creating a Django App**  
A Django project can have multiple **apps**, which are modular components. To create an app:  
```bash
python manage.py startapp myapp
```
This creates a new folder **myapp/** with:  
```
myapp/
│── models.py       # Database models
│── views.py        # View functions (business logic)
│── urls.py         # URL routing for this app
│── templates/      # HTML templates
│── static/         # CSS, JavaScript, images
```

**Register the app in `settings.py`**:  
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Register your app
]
```

---

## **5. URLs and Views**  
### **Defining URLs**  
In `myapp/urls.py` (create the file if it doesn’t exist):  
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```
Then, in `views.py`:  
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```
Finally, include the app’s URLs in the project’s `urls.py`:  
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include myapp’s URLs
]
```
Restart the server, and visiting **http://127.0.0.1:8000/** should show `"Hello, Django!"`.

---

## **6. Models and Database**  
Django provides an ORM (Object-Relational Mapping) to interact with databases.  

### **Defining a Model**  
In `models.py`:  
```python
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name
```
Run migrations:  
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## **7. Django Admin Panel**  
Create a superuser:  
```bash
python manage.py createsuperuser
```
Register the model in `admin.py`:  
```python
from django.contrib import admin
from .models import Employee

admin.site.register(Employee)
```
Now, go to **http://127.0.0.1:8000/admin/** and log in.

---

## **8. Django Templates**  
Django uses **templates** to separate the frontend (HTML) from backend logic.  

Create a folder `templates/myapp/home.html` and add:  
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Django</h1>
</body>
</html>
```
Modify `views.py` to render it:  
```python
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')
```

---

## **9. Django Forms**  
Django makes handling forms easy.  

### **Creating a Form**  
Create `forms.py`:  
```python
from django import forms

class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    department = forms.CharField(max_length=50)
```
### **Using the Form in Views**  
Modify `views.py`:  
```python
from django.shortcuts import render
from .forms import EmployeeForm

def home(request):
    form = EmployeeForm()
    return render(request, 'myapp/home.html', {'form': form})
```
### **Updating the Template (`home.html`)**  
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

---

## **10. Django REST Framework (DRF) for APIs**  
For building REST APIs, install DRF:  
```bash
pip install djangorestframework
```
Add `'rest_framework'` to `INSTALLED_APPS`.  

Create an API in `views.py`:  
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_home(request):
    return Response({"message": "Hello, API!"})
```
Update `urls.py`:  
```python
from django.urls import path
from .views import api_home

urlpatterns = [
    path('api/', api_home),
]
```
Visit **http://127.0.0.1:8000/api/** to see the response.

---

## **11. Deployment (Basics)**  
To deploy a Django app:  
- Use **Gunicorn** and **NGINX** for production.  
- Use **PostgreSQL** instead of SQLite for a real database.  
- Use **Django’s `whitenoise`** for serving static files.  

Example commands for deployment:  
```bash
pip install gunicorn
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
```

---

## **Next Steps**  
1. **Learn Django Class-Based Views (CBVs)** – A more organized way to write views.  
2. **Work with Django Authentication** – User logins, permissions, etc.  
3. **Use Django ORM for complex queries** – Filtering, joins, etc.  
4. **Build a Real-World Project** – Blog, e-commerce, etc.  

---

This is a strong foundation! Do you want to focus on anything specific, like **DRF, authentication, or deployment**?