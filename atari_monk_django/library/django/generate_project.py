import os
import subprocess
import sys
from .setup_django import check_django_installed

def generate_project(project_name=None, skip_migrations=False, skip_runserver=False):
    if project_name is None:
        project_name = input("📌 Enter your Django project name: ").strip()
        if not project_name:
            print("⚠️ Project name cannot be empty. Try again.")
            return

    if not check_django_installed(verbose=True):
        print("❌ Django is not installed. Run `pip install django` and try again.")
        return

    current_dir = os.getcwd()
    project_path = os.path.join(current_dir, project_name)

    if os.path.exists(project_path):
        print(f"⚠️ A folder named '{project_name}' already exists in {current_dir}. Choose a different name.")
        return

    print(f"\n🚀 Creating Django project '{project_name}' in {current_dir}...\n")

    try:
        subprocess.check_call(["django-admin", "startproject", project_name])
        print(f"✅ Django project '{project_name}' created successfully!\n")

        os.chdir(project_path)

        if not skip_migrations:
            print("\n🔄 Applying migrations...\n")
            subprocess.check_call(["python", "manage.py", "migrate"])
            print("✅ Migrations applied successfully!")
        else:
            print("\n⏩ Skipping migrations as requested\n")

        if not skip_runserver:
            print("\n🚀 Starting Django server...\n")
            if sys.platform == "win32":
                subprocess.Popen(["start", "cmd", "/k", "python manage.py runserver"], shell=True)
            elif sys.platform == "darwin":
                subprocess.Popen(["osascript", "-e", f'tell application "Terminal" to do script "cd {project_path} && python manage.py runserver"'])
            else:
                subprocess.Popen(["gnome-terminal", "--", "python", "manage.py", "runserver"])
            print("\n🌍 Server started in a new terminal. Close that window or press CTRL + C to stop the server.")
        else:
            print("\n⏩ Skipping server startup as requested\n")

    except subprocess.CalledProcessError as e:
        print(f"❌ An error occurred while setting up the project: {e}")