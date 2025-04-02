#!/usr/bin/env python
from pathlib import Path

def generate_crud(app_name=None, model_name=None):
    """
    Generates CRUD views, URLs, and templates for an existing Django model.
    Uses interactive input if parameters aren't provided.
    """
    
    # Interactive mode
    if not app_name:
        app_name = input("Enter your Django app name: ").strip()
    if not model_name:
        model_name = input(f"Enter model name in {app_name} (e.g., 'Link'): ").strip()

    # 1. Generate Views File
    views_content = f"""from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import {model_name}

class {model_name}ListView(ListView):
    model = {model_name}
    template_name = '{app_name}/{model_name.lower()}_list.html'
    context_object_name = '{model_name.lower()}_list'

class {model_name}CreateView(CreateView):
    model = {model_name}
    fields = '__all__'
    template_name = '{app_name}/{model_name.lower()}_form.html'
    success_url = '/{app_name}/'

class {model_name}UpdateView(UpdateView):
    model = {model_name}
    fields = '__all__'
    template_name = '{app_name}/{model_name.lower()}_form.html'
    success_url = '/{app_name}/'

class {model_name}DeleteView(DeleteView):
    model = {model_name}
    template_name = '{app_name}/{model_name.lower()}_confirm_delete.html'
    success_url = '/{app_name}/'
"""
    
    # 2. Generate URLs File
    urls_content = f"""from django.urls import path
from .views import (
    {model_name}ListView,
    {model_name}CreateView,
    {model_name}UpdateView,
    {model_name}DeleteView
)

app_name = '{app_name}'

urlpatterns = [
    path('', {model_name}ListView.as_view(), name='list'),
    path('create/', {model_name}CreateView.as_view(), name='create'),
    path('<int:pk>/edit/', {model_name}UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', {model_name}DeleteView.as_view(), name='delete'),
]
"""
    
    # 3. Generate Templates
    templates = {
        f"{model_name.lower()}_list.html": f"""<h1>{model_name} List</h1>
<a href="{{% url '{app_name}:create' %}}">Add New</a>
<ul>
    {{% for obj in {model_name.lower()}_list %}}
    <li>
        {{ obj }}
        <a href="{{% url '{app_name}:update' obj.pk %}}">Edit</a>
        <a href="{{% url '{app_name}:delete' obj.pk %}}">Delete</a>
    </li>
    {{% endfor %}}
</ul>
""",
        f"{model_name.lower()}_form.html": f"""<h1>{{% if object %}}Edit{{% else %}}Create{{% endif %}} {model_name}</h1>
<form method="post">
    {{% csrf_token %}}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
<a href="{{% url '{app_name}:list' %}}">Cancel</a>
""",
        f"{model_name.lower()}_confirm_delete.html": f"""<h1>Delete {model_name}</h1>
<p>Are you sure you want to delete "{{ object }}"?</p>
<form method="post">
    {{% csrf_token %}}
    <button type="submit">Confirm Delete</button>
    <a href="{{% url '{app_name}:list' %}}">Cancel</a>
</form>
"""
    }
    
    # Create directories
    base_dir = Path.cwd()
    app_dir = base_dir / app_name
    templates_dir = app_dir / 'templates' / app_name
    templates_dir.mkdir(parents=True, exist_ok=True)
    
    # Write files
    (app_dir / 'views.py').write_text(views_content)
    (app_dir / 'urls.py').write_text(urls_content)
    
    for filename, content in templates.items():
        (templates_dir / filename).write_text(content)
    
    print(f"""
✅ CRUD operations generated for {model_name} in {app_name}!

Next steps:
1. Include in project urls.py:
   path('{app_name}/', include('{app_name}.urls')),

2. Run migrations (if model changed):
   python manage.py makemigrations
   python manage.py migrate

3. Start development server:
   python manage.py runserver

4. Access at:
   http://localhost:8000/{app_name}/
""")
