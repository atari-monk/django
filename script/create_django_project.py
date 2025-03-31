import os
import subprocess

def create_django_project():
    project_name = input("📌 Enter your Django project name: ").strip()
    
    if not project_name:
        print("⚠️ Project name cannot be empty. Try again.")
        return

    parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
    project_path = os.path.join(parent_dir, project_name)

    if os.path.exists(project_path):
        print(f"⚠️ A folder named '{project_name}' already exists in {parent_dir}. Choose a different name.")
        return
    
    print(f"\n🚀 Creating Django project '{project_name}' in {parent_dir}...\n")

    try:
        subprocess.check_call(["django-admin", "startproject", project_name, parent_dir])
        print(f"✅ Django project '{project_name}' created successfully in {parent_dir}!\n")

        os.chdir(project_path)

        print("\n🚀 Starting the Django development server...\n")
        subprocess.check_call(["python", "manage.py", "runserver"])
        
        print("\n🌍 Visit http://127.0.0.1:8000/ to see your project running.")
    
    except subprocess.CalledProcessError:
        print("❌ An error occurred while setting up the project.")
    except FileNotFoundError:
        print("❌ Django is not installed. Run `pip install django` and try again.")

if __name__ == "__main__":
    create_django_project()
