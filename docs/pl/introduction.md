# Django

# Wprowadzenie

Pytanie 1: Firma pracuje z Django. Muszę wiedzieć o nim wszystko, aby przygotować się do pracy. Czy możesz mnie nauczyć?

Content_1: Tak! Django to potężny framework internetowy do tworzenia aplikacji internetowych przy użyciu Pythona. Omówię go krok po kroku, aby pomóc Ci go opanować w ramach przygotowania do pracy.

## **1. Wprowadzenie do Django**  

Treść_1: Django to **zaawansowany framework webowy w Pythonie**, który wspiera **szybki rozwój** i **czysty, pragmatyczny design**. Opiera się na wzorcu **MVC (Model-View-Controller)**, choć w Django nazywa się to **MTV (Model-Template-View)**.  

### **Dlaczego Django?**  
✅ **Szybki rozwój** – Wbudowane funkcje jak uwierzytelnianie, ORM, panel administracyjny itp.  
✅ **Bezpieczeństwo** – Ochrona przed SQL injection, CSRF, XSS itp.  
✅ **Skalowalność** – Obsługuje duże aplikacje przy odpowiedniej optymalizacji.  
✅ **„Baterie w zestawie”** – Wiele funkcji wbudowanych, np. formularze, sesje użytkowników.  

---

## **2. Instalacja Django**  
### **Instalacja**  
Upewnij się, że masz zainstalowanego Pythona (najlepiej 3.8+). Następnie zainstaluj Django:  
```bash
pip install django
```
Sprawdzenie instalacji:  
```bash
django-admin --version
```

---

## **3. Tworzenie projektu Django**  
Stwórz nowy projekt Django:  
```bash
django-admin startproject myproject
cd myproject
python manage.py runserver
```
Otwórz **http://127.0.0.1:8000/** w przeglądarce – zobaczysz domyślną stronę Django.  

### **Struktura projektu Django**  
```
myproject/
│── manage.py        # Narzędzie CLI Django
│── myproject/       # Pliki konfiguracyjne projektu
│   │── settings.py  # Ustawienia projektu (baza danych, aplikacje)
│   │── urls.py      # Routing URL
│   │── wsgi.py      # Punkt wejścia dla WSGI
│   │── asgi.py      # Punkt wejścia dla ASGI
│── app/             # Każda aplikacja Django (do utworzenia)
```

---

## **4. Tworzenie aplikacji Django**  
Django pozwala na podział projektu na moduły zwane **aplikacjami**. Aby stworzyć aplikację:  
```bash
python manage.py startapp myapp
```
To utworzy folder **myapp/** z plikami:  
```
myapp/
│── models.py       # Modele bazy danych
│── views.py        # Logika aplikacji
│── urls.py         # Routing URL dla aplikacji
│── templates/      # Szablony HTML
│── static/         # Pliki statyczne (CSS, JS, obrazy)
```

**Dodaj aplikację do `settings.py`**:  
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Rejestracja aplikacji
]
```

---

## **5. Routing URL i widoki**  
### **Definiowanie URL-i**  
W `myapp/urls.py` (stwórz plik, jeśli nie istnieje):  
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```
W `views.py`:  
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```
Teraz do `myproject/urls.py` dodaj:  
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Dodanie URL aplikacji
]
```
Uruchom ponownie serwer i otwórz **http://127.0.0.1:8000/** – powinien wyświetlić się tekst `"Hello, Django!"`.

---

## **6. Modele i baza danych**  
Django używa ORM (Object-Relational Mapping) do obsługi baz danych.  

### **Definiowanie modelu**  
W `models.py`:  
```python
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name
```
Migracje do bazy danych:  
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## **7. Panel administracyjny Django**  
Stwórz superużytkownika:  
```bash
python manage.py createsuperuser
```
Zarejestruj model w `admin.py`:  
```python
from django.contrib import admin
from .models import Employee

admin.site.register(Employee)
```
Teraz otwórz **http://127.0.0.1:8000/admin/** i zaloguj się.

---

## **8. Szablony Django**  
Django używa **szablonów HTML** do oddzielenia warstwy frontendowej od backendu.  

Utwórz folder `templates/myapp/home.html` i dodaj:  
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Witaj w Django!</h1>
</body>
</html>
```
Zmień `views.py`, aby renderować szablon:  
```python
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')
```

---

## **9. Formularze Django**  
Django ułatwia obsługę formularzy.  

### **Tworzenie formularza**  
Stwórz `forms.py`:  
```python
from django import forms

class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    department = forms.CharField(max_length=50)
```
### **Obsługa formularza w widokach**  
Zmień `views.py`:  
```python
from django.shortcuts import render
from .forms import EmployeeForm

def home(request):
    form = EmployeeForm()
    return render(request, 'myapp/home.html', {'form': form})
```
### **Aktualizacja szablonu (`home.html`)**  
```html
{% raw %}
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
{% endraw %}
```

---

## **10. Django REST Framework (DRF) – API**  
Django REST Framework (DRF) ułatwia budowę API. Instalacja:  
```bash
pip install djangorestframework
```
Dodaj `'rest_framework'` do `INSTALLED_APPS`.  

Stwórz API w `views.py`:  
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_home(request):
    return Response({"message": "Hello, API!"})
```
Dodaj URL w `urls.py`:  
```python
from django.urls import path
from .views import api_home

urlpatterns = [
    path('api/', api_home),
]
```
Otwórz **http://127.0.0.1:8000/api/**, aby zobaczyć odpowiedź JSON.

---

## **11. Wdrażanie Django (podstawy)**  
Aby wdrożyć aplikację:  
- Użyj **Gunicorn** i **NGINX** w środowisku produkcyjnym.  
- Przejdź na **PostgreSQL** zamiast SQLite.  
- Użyj **Django Whitenoise** do obsługi plików statycznych.  

Przykładowe polecenie do uruchomienia aplikacji:  
```bash
pip install gunicorn
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
```

---

## **Co dalej?**  
1. **Zrozumienie Django Class-Based Views (CBVs)**.  
2. **Praca z autoryzacją i uwierzytelnianiem użytkowników**.  
3. **Zaawansowane zapytania ORM** – filtrowanie, łączenie tabel.  
4. **Budowa realnego projektu** – np. blog, sklep internetowy.  

To solidna podstawa! Chcesz skupić się na czymś konkretnym, np. **DRF, autoryzacji czy wdrażaniu**? 🚀