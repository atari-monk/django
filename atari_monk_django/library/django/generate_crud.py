#!/usr/bin/env python
import os
import sys
from pathlib import Path
import subprocess

def find_django_project():
    """Locate Django project root by finding manage.py"""
    path = Path.cwd()
    while not (path / 'manage.py').exists():
        if path == path.parent:
            raise FileNotFoundError("Couldn't find manage.py - are you in a Django project?")
        path = path.parent
    return path

def generate_crud(app_name, model_name):
    """Generate complete CRUD system for a model"""
    try:
        project_path = find_django_project()
        os.chdir(project_path)
        
        if not app_name:
            app_name = input("Enter your Django app name: ").strip()
        if not model_name:
            model_name = input(f"Enter model name in {app_name} (e.g., 'Link'): ").strip()

        app_dir = project_path / app_name
        templates_dir = app_dir / 'templates' / app_name
        
        # 1. Generate CRUD Views
        views_content = f"""from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import {model_name}

class {model_name}ListView(ListView):
    model = {model_name}
    template_name = '{app_name}/{model_name.lower()}_list.html'
    context_object_name = 'items'
    paginate_by = 10

class {model_name}CreateView(CreateView):
    model = {model_name}
    fields = '__all__'
    template_name = '{app_name}/{model_name.lower()}_form.html'
    success_url = reverse_lazy('{app_name}:list')

class {model_name}UpdateView(UpdateView):
    model = {model_name}
    fields = '__all__'
    template_name = '{app_name}/{model_name.lower()}_form.html'
    success_url = reverse_lazy('{app_name}:list')

class {model_name}DeleteView(DeleteView):
    model = {model_name}
    template_name = '{app_name}/{model_name.lower()}_confirm_delete.html'
    success_url = reverse_lazy('{app_name}:list')
"""
        
        # 2. Generate URLs
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
<a href="{{% url '{app_name}:create' %}}" class="btn btn-primary mb-3">Add New</a>

<table class="table">
    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {{% for item in items %}}
        <tr>
            <td>{{ item.id }}</td>
            <td>{{ item }}</td>
            <td>
                <a href="{{% url '{app_name}:update' item.pk %}}" class="btn btn-sm btn-warning">Edit</a>
                <a href="{{% url '{app_name}:delete' item.pk %}}" class="btn btn-sm btn-danger">Delete</a>
            </td>
        </tr>
        {{% endfor %}}
    </tbody>
</table>

{{% if is_paginated %}}
<div class="pagination">
    <span class="page-links">
        {{% if page_obj.has_previous %}}
            <a href="?page={{ page_obj.previous_page_number }}">previous</a>
        {{% endif %}}
        <span class="page-current">
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
        </span>
        {{% if page_obj.has_next %}}
            <a href="?page={{ page_obj.next_page_number }}">next</a>
        {{% endif %}}
    </span>
</div>
{{% endif %}}
""",
            f"{model_name.lower()}_form.html": f"""<h1>{{% if object %}}Edit{{% else %}}Create{{% endif %}} {model_name}</h1>
<form method="post" class="mt-4">
    {{% csrf_token %}}
    <table class="table">
    {{ form.as_table }}
    </table>
    <button type="submit" class="btn btn-success">Save</button>
    <a href="{{% url '{app_name}:list' %}}" class="btn btn-secondary">Cancel</a>
</form>
""",
            f"{model_name.lower()}_confirm_delete.html": f"""<div class="card">
    <div class="card-header">
        <h1>Delete {model_name}</h1>
    </div>
    <div class="card-body">
        <p>Are you sure you want to delete "{{ object }}"?</p>
        <form method="post">
            {{% csrf_token %}}
            <button type="submit" class="btn btn-danger">Confirm Delete</button>
            <a href="{{% url '{app_name}:list' %}}" class="btn btn-secondary">Cancel</a>
        </form>
    </div>
</div>
"""
        }

        # Create directories
        app_dir = project_path / app_name
        templates_dir = app_dir / 'templates' / app_name
        templates_dir.mkdir(parents=True, exist_ok=True)

        # Write files
        (app_dir / 'views.py').write_text(views_content)
        (app_dir / 'urls.py').write_text(urls_content)
        for filename, content in templates.items():
            (templates_dir / filename).write_text(content)

        # 4. Update project URLs
        project_urls = project_path / 'urls.py'
        if project_urls.exists():
            content = project_urls.read_text()
            if f"include('{app_name}.urls')" not in content:
                new_content = content.replace(
                    'from django.urls import path',
                    'from django.urls import path, include'
                ).replace(
                    'urlpatterns = [',
                    f'urlpatterns = [\n    path(\'{app_name}/\', include(\'{app_name}.urls\')),'
                )
                project_urls.write_text(new_content)

        print(f"""
✅ CRUD for {model_name} successfully generated!

Access your CRUD interface at:
http://localhost:8000/{app_name}/

Included features:
- List view with pagination
- Create/Update forms
- Delete confirmation
- Bootstrap-styled templates
- Proper URL reversing
""")

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
